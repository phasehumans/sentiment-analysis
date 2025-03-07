# **Literature Review**  

## **1. Summary of Existing Technologies, Methods, and Solutions**  

### **1.1 Sentiment Analysis in Social Media**  
Sentiment analysis is widely used in social media platforms like **Twitter, Facebook, and YouTube** to analyze public opinion. Various techniques exist for sentiment classification, including:  
- **Lexicon-Based Approaches** – Use predefined sentiment word dictionaries (e.g., TextBlob, VADER).  
- **Machine Learning-Based Approaches** – Utilize algorithms like Naïve Bayes, SVM, and Logistic Regression.  
- **Deep Learning-Based Approaches** – Employ neural networks like LSTMs, BERT, and RoBERTa for advanced sentiment detection.  

Studies indicate that sentiment analysis is crucial for **brand monitoring, customer feedback analysis, and social media trend prediction**.  

### **1.2 Sentiment Analysis Using Lexicon-Based Methods**  
Lexicon-based methods, such as **TextBlob and VADER**, assign sentiment scores based on predefined word lists. These methods are useful for basic sentiment analysis but have significant limitations in handling:  
- **Contextual meanings** – They cannot understand word relationships.  
- **Sarcasm and slang** – They misclassify ironic or informal language.  

#### **Examples of Lexicon-Based Methods:**  
- **TextBlob** – A simple NLP library that assigns sentiment scores based on a word polarity dictionary.  
- **VADER (Valence Aware Dictionary and sEntiment Reasoner)** – More effective for short, informal texts like tweets and YouTube comments.  

**Limitations:** These methods **do not learn from data**, making them less effective for complex language patterns.  

### **1.3 Machine Learning for Sentiment Analysis**  
Traditional machine learning models require **labeled datasets** to learn sentiment classification. Some of the widely used models include:  
- **Naïve Bayes** – A probabilistic classifier effective for short text.  
- **Support Vector Machines (SVM)** – Finds the optimal decision boundary for classification.  
- **Logistic Regression** – A linear model effective for binary classification.  

**Limitations:**  
- Requires **manual feature engineering** (e.g., TF-IDF, word embeddings).  
- Struggles with **high-dimensional data** if features are not well-selected.  

### **1.4 Deep Learning for Sentiment Analysis**  
Advanced NLP techniques use deep learning models like:  
- **LSTMs and GRUs** – Handle sequential text but require extensive training data.  
- **Transformer Models (BERT, RoBERTa, GPT)** – Achieve high accuracy by understanding word relationships and context.  

**Limitations:**  
- Computationally expensive and requires **large datasets**.  
- Training models like BERT require **high-end GPUs and significant processing power**.  
 

## **2. Why Machine Learning for This Project?**  
Based on the literature review, this project adopts a **Machine Learning-based approach** for sentiment analysis due to:  
- **Higher Accuracy** – ML models perform better than rule-based methods in complex sentence structures.  
- **Improved Generalization** – Trained models adapt to new datasets better than static word dictionaries.  
- **Scalability** – Works efficiently for large-scale comment extraction and classification.  

### **Key Model Choices for This Project:**  
- **TF-IDF for Feature Extraction** – Converts text into numerical vectors efficiently.  
- **Naïve Bayes / Logistic Regression / SVM** – Selected for their balance of accuracy and efficiency.  
- **Flask-based Web App** – Ensures real-time analysis and easy deployment.  

This approach **ensures better sentiment classification** while keeping computational requirements manageable.  
