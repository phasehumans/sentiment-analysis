from flask import Flask, render_template, request
from sentiment_utils import analyze_youtube_video
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('video_url', '').strip()
        
        if not video_url:
            return render_template('index.html', error="Please enter a YouTube URL")
        
        if 'youtube.com' not in video_url and 'youtu.be' not in video_url:
            return render_template('index.html', error="Please enter a valid YouTube URL")
        
        try:
            results = analyze_youtube_video(video_url)
            if not results['video_id']:
                return render_template('index.html', 
                                    error="Couldn't extract video ID. Try a different URL format.")
            return render_template('index.html', results=results)
        except Exception as e:
            return render_template('index.html', 
                                error=f"Error analyzing video: {str(e)}")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)