# **Semester Project - II: YouTube Comment Sentiment Analysis**  

**Domain:** Machine Learning

**Application:** Sentiment Analysis of YouTube Comments  

**Processing:**  
- Extraction of comments using the YouTube Data API  
- **Machine Learning-based sentiment classification** instead of rule-based TextBlob  
- Text preprocessing (Cleaning, Tokenization, Stopword Removal, Lemmatization)  
- Feature Extraction using TF-IDF  
- Training a classification model (Logistic Regression)  

## **Abstract**  
The **YouTube Comment Sentiment Analysis System** is a web-based application that extracts comments from YouTube videos and classifies them into **Positive, Negative, or Neutral** sentiments using **Machine Learning**. The system leverages the **YouTube Data API** to fetch comments and applies **Natural Language Processing (NLP) techniques** to clean and preprocess the text.  

Instead of a rule-based approach like TextBlob, this project implements a **trained Machine Learning model** to enhance accuracy and generalizability. It applies **TF-IDF vectorization** to convert text into numerical representations and utilizes a **classification algorithm** Logistic Regression to predict sentiment labels.  

This system is beneficial for **content creators, brands, and researchers** to assess public opinion on videos, identify trends, and make data-driven decisions.

## **Phases of Development:**  
1. **Data Collection**   
   - Use an existing **labeled dataset** for training  

2. **Data Processing**  
   - Remove URLs, emojis, and special characters  
   - Convert text to lowercase  
   - Remove stopwords  
   - Tokenization and Lemmatization  

3. **Feature Extraction**  
   - Convert text into numerical form using **TF-IDF vectorization**  

4. **Model Training & Evaluation**  
   - Train a **classification model** Logistic Regression 

5. **Web Application Development**  
   - Build a **Flask-based UI** for user interaction  
   - Accept YouTube video URLs and process comments  

6. **Deployment**  
   - Deploy using **Flask and cloud platforms** for real-time sentiment analysis  

## **Team Members:**  
- **Sakshi Dadabhau Patil** SYAIML-06 (231107004)  
- **Tanisha Chudaman Badgujar** SYAIML-26 (231107027)  
- **Priyanshu Dipak Patil** SYAIML-62 (241207003)  
- **Chetan Prabhakar Sonawane** SYAIML-40 (231107042)  
