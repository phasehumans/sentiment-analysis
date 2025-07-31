from flask import Flask, render_template, request
import pickle
import os
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

# Initialize NLTK components
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

# YouTube API configuration
API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def load_model():
    """Load the pre-trained model and vectorizer"""
    model_path = os.path.join("models", "sentiment_model.pkl")
    vectorizer_path = os.path.join("models", "tfidf_vectorizer.pkl")
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vectorizer_path, "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

def extract_video_id(url):
    """Extract YouTube video ID from various URL formats"""
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]+)',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/v\/([a-zA-Z0-9_-]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_youtube_comments(video_id, max_results=100):
    """Fetch comments from YouTube video"""
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    comments = []
    next_page_token = None
    
    try:
        while len(comments) < max_results:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=min(100, max_results - len(comments)),
                pageToken=next_page_token,
                textFormat="plainText"
            )
            response = request.execute()
            
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)
            
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
                
    except HttpError as e:
        print(f"Error fetching comments: {e}")
        if e.resp.status == 403:
            print("Comments are disabled for this video")
        return []
    
    return comments[:max_results]

def clean_text(text):
    """Clean and preprocess text matching your model's requirements"""
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters
    text = ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(text)])  # Lemmatization
    return text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_url = request.form.get('video_url')
    
    if not video_url:
        return render_template('index.html', error="Please enter a YouTube URL")
    
    try:
        # Extract video ID and get comments
        video_id = extract_video_id(video_url)
        if not video_id:
            return render_template('index.html', error="Invalid YouTube URL")
        
        comments = get_youtube_comments(video_id)
        if not comments:
            return render_template('index.html', error="No comments found or comments disabled")
        
        # Load model and analyze comments
        model, vectorizer = load_model()
        sentiments = []
        
        for comment in comments:
            cleaned = clean_text(comment)
            vectorized = vectorizer.transform([cleaned])
            prediction = model.predict(vectorized)[0]
            sentiments.append(prediction)
        
        # Calculate results
        total = len(sentiments)
        positive = sentiments.count('positive')
        negative = sentiments.count('negative')
        neutral = sentiments.count('neutral')
        
        results = {
            'total': total,
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
            'positive_pct': round(positive/total*100, 2),
            'negative_pct': round(negative/total*100, 2),
            'neutral_pct': round(neutral/total*100, 2),
            'video_url': video_url,
            'overall': max(set(sentiments), key=sentiments.count)
        }
        
        return render_template('results.html', results=results)
    
    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)