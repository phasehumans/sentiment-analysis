from models.load_model import load_model
from googleapiclient.discovery import build
import re
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()

model, vectorizer = load_model()

def extract_video_id(url):
    """Extract YouTube video ID from URL with comprehensive pattern matching"""
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/live\/([a-zA-Z0-9_-]{11})',
        r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/.*[&?]v=([a-zA-Z0-9_-]{11})',
        r'^([a-zA-Z0-9_-]{11})$'
    ]
    
    for pattern in patterns:
        try:
            match = re.search(pattern, url)
            if match and match.group(1):
                return match.group(1)
        except re.error:
            continue
            
    return None

def clean_text(text):
    text = str(text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.strip().lower()

def predict_sentiment(comment):
    clean_comment = clean_text(comment)
    vectorized_comment = vectorizer.transform([clean_comment])
    return model.predict(vectorized_comment)[0]

def get_youtube_comments(video_url, max_comments=50):
    """Fetch comments from YouTube video with better error handling"""
    video_id = extract_video_id(video_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL - could not extract video ID")
    
    try:
        youtube = build('youtube', 'v3', developerKey=os.getenv('YOUTUBE_API_KEY'))
        
        comments = []
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_comments,
            textFormat="plainText",
            order="relevance"
        )
        
        while request and len(comments) < max_comments:
            response = request.execute()
            
            if 'items' not in response:
                raise ValueError("Comments are disabled for this video")
                
            comments.extend(
                item['snippet']['topLevelComment']['snippet']['textDisplay']
                for item in response['items']
            )
            request = youtube.commentThreads().list_next(request, response)
        
        return comments[:max_comments]
        
    except Exception as api_error:
        raise ValueError(f"Error fetching comments: {str(api_error)}")

def analyze_youtube_video(video_url):
    """Main function to analyze a YouTube video"""
    comments = get_youtube_comments(video_url)
    
    results = {
        'video_id': extract_video_id(video_url),
        'comments': [],
        'counts': {'positive': 0, 'neutral': 0, 'negative': 0},
        'examples': {'positive': [], 'neutral': [], 'negative': []}
    }
    
    for comment in comments:
        sentiment = predict_sentiment(comment)
        results['comments'].append({'text': comment, 'sentiment': sentiment})
        results['counts'][sentiment] += 1
        
        if len(results['examples'][sentiment]) < 3:
            results['examples'][sentiment].append(comment)
    
    total = len(comments)
    results['percentages'] = {
        'positive': round(results['counts']['positive'] / total * 100),
        'neutral': round(results['counts']['neutral'] / total * 100),
        'negative': round(results['counts']['negative'] / total * 100)
    }
    
    return results