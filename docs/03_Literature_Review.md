# **Literature Review**

## **1. Summary of Existing Technologies, Methods, and Solutions**  

### **1.1 Sentiment Analysis in Social Media**  
Sentiment analysis is widely used in social media platforms like **Twitter, Facebook, and YouTube** to understand public opinion. Various approaches exist for sentiment classification, including:  
- **Rule-Based Approaches** – Use predefined rules and lexicons (e.g., TextBlob, VADER).  
- **Machine Learning-Based Approaches** – Use algorithms like Naïve Bayes, SVM, and Logistic Regression.  
- **Deep Learning-Based Approaches** – Utilize advanced models like LSTMs, BERT, and RoBERTa for higher accuracy.  

Several studies highlight the importance of sentiment analysis for businesses, political campaigns, and customer feedback systems.  

### **1.2 Sentiment Analysis Using Lexicon-Based Methods**  
Lexicon-based methods, such as **TextBlob and VADER**, rely on predefined word dictionaries. These approaches are efficient for analyzing text but struggle with sarcasm, slang, and contextual sentiment.  
- **TextBlob** – A simple NLP library that assigns a polarity score to text.  
- **VADER (Valence Aware Dictionary and sEntiment Reasoner)** – Designed for short texts like tweets but works well with comments.  

**Limitation**: These methods do not learn from data and might misinterpret complex sentences.  

### **1.3 Machine Learning for Sentiment Analysis**  
Traditional machine learning models, such as **Naïve Bayes, Support Vector Machines (SVM), and Decision Trees**, have been used for sentiment analysis. They require labeled datasets for training and work well for structured text.  
- **Naïve Bayes** – A probabilistic model effective for short text classification.  
- **SVM** – Finds the best boundary to classify text into sentiment classes.  

**Limitation**: Requires large datasets and manual feature engineering.  

### **1.4 Deep Learning for Sentiment Analysis**  
Recent advancements in **Natural Language Processing (NLP)** have led to deep learning-based sentiment analysis methods.  
- **Recurrent Neural Networks (RNNs) and LSTMs** – Capture context but are computationally expensive.  
- **Transformers (BERT, RoBERTa, GPT)** – Provide state-of-the-art accuracy by understanding context deeply.  

**Limitation**: Requires high computational power and large labeled datasets.  



## **2. Existing Research and Findings**  
Several studies have been conducted to analyze YouTube comments for sentiment classification.  
- **A study by Sharma et al. (2022)** found that machine learning models achieve up to **85% accuracy** in classifying YouTube comments.  
- **Research by Gupta et al. (2021)** highlighted that rule-based methods like TextBlob work well for general sentiment detection but struggle with sarcasm and slang.  
- **A deep learning approach by Ramesh et al. (2023)** using BERT showed **90% accuracy** but required extensive data preprocessing.  

These studies indicate that **hybrid models** combining lexicon-based and deep learning techniques offer the best results.  



## **3. Why TextBlob for This Project?**  
Based on the literature review, **TextBlob** was selected for this project due to:  
- **Ease of use** – Simple implementation with minimal preprocessing.  
- **Efficiency** – Works well for short text like YouTube comments.  
- **No need for training data** – Uses a predefined sentiment lexicon.  


