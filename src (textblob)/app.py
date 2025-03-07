from flask import Flask, render_template, request
import googleapiclient.discovery
import googleapiclient.errors
from textblob import TextBlob
import pandas as pd
import re

app = Flask(__name__)

# Step 1: Extract Video ID from YouTube Link
def extract_video_id(youtube_link):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, youtube_link)
    return match.group(1) if match else None  # Return None for invalid links

# Step 2: Fetch Comments from YouTube Video (Handling API Errors)
def get_video_comments(api_key, video_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    comments = []

    try:
        # Check if comments are enabled
        video_details = youtube.videos().list(part="statistics", id=video_id).execute()
        if 'commentCount' not in video_details['items'][0]['statistics']:
            return "disabled"  # Comments are disabled

        # Fetch comments
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=100
        )
        
        while request:
            response = request.execute()
            for item in response.get('items', []):
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)
            request = youtube.commentThreads().list_next(request, response)

    except googleapiclient.errors.HttpError as e:
        return None  # API error occurred

    return comments if comments else "empty"  # Return "empty" if no comments

# Step 3: Perform Sentiment Analysis
def analyze_sentiment(comments):
    sentiments = []
    for comment in comments:
        blob = TextBlob(comment)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiments.append("Positive")
        elif polarity < 0:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")
    return sentiments

# Step 4: Flask Route for Home Page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        api_key = "AIzaSyCU9GGlMAm6n6_n3yg8ePtuiixB79QCEP0"  # Replace with your actual API key
        youtube_link = request.form["youtube_link"]
        
        video_id = extract_video_id(youtube_link)
        if not video_id:
            return render_template("index.html", error="Invalid YouTube URL!")

        comments = get_video_comments(api_key, video_id)
        if comments == "disabled":
            return render_template("index.html", error="Comments are disabled for this video.")
        elif comments == "empty":
            return render_template("index.html", error="No comments found on this video.")
        elif comments is None:
            return render_template("index.html", error="Failed to fetch comments. Please try again.")

        sentiments = analyze_sentiment(comments)
        sentiment_counts = pd.Series(sentiments).value_counts().to_dict()
        
        return render_template("result.html", comments=comments, sentiment_counts=sentiment_counts)

    return render_template("index.html")

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
