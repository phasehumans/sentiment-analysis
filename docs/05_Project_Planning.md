# **Project Planning and Design**

---

## **i. Methodology / Approach Used**

The project follows a structured, step-by-step approach to implement a sentiment analysis system using **Naïve Bayes**.

### **1. Data Collection**
- We collected a dataset of YouTube comments.
- The dataset includes a large number of manually or publicly labeled comments with sentiment tags: **Positive**, **Negative**, or **Neutral**.

### **2. Preprocessing**
- Text data is cleaned by removing:
  - Special characters
  - URLs
  - Stopwords (like “is”, “the”, “and”)
  - Punctuation and emojis
- Text is converted to lowercase and lemmatized for normalization.

### **3. Feature Extraction**
- **TF-IDF (Term Frequency-Inverse Document Frequency)** is used to convert text into numerical format for training.
- It helps identify important words in the context of the document corpus.

### **4. Model Building**
- A **Naïve Bayes classifier** is trained using the preprocessed TF-IDF vectors.
- Model performance is evaluated using metrics like:
  - Accuracy
  - Precision
  - Recall
  - Confusion matrix

### **5. Saving the Model**
- Once trained, the model and TF-IDF vectorizer are saved using `joblib` for use in the Flask application.

### **6. Flask Web Application Integration**
- A web interface is created using Flask.
- User inputs a **YouTube video URL**.
- The app fetches comments using the **YouTube Data API**.
- The saved Naïve Bayes model classifies the sentiment of each comment.
- Final sentiment analysis results are displayed on the webpage.

---

## **ii. Materials, Tools, and Software Required**

### **Programming Language**
- **Python 3.8+**

### **Libraries and Frameworks**
- **Flask** – Web application framework
- **scikit-learn** – For training the Naïve Bayes classifier and TF-IDF vectorization
- **pandas, numpy** – For data manipulation
- **matplotlib, seaborn** – For data visualization and EDA
- **Text preprocessing tools** – Regex, nltk, or spaCy for cleaning
- **joblib or pickle** – For saving the trained model and vectorizer

### **APIs and External Services**
- **YouTube Data API v3** – To fetch comments from a video
- **Google Cloud Console** – To generate an API key for YouTube

### **Development Tools**
- **VS Code / PyCharm** – Code editors
- **Postman** – API testing
- **GitHub** – For version control
- **Render** – Deployment platforms for web hosting

---

## **Workflow Summary**
1. Data Collection → 
2. Cleaning & Preprocessing → 
3. TF-IDF Transformation →  
4. Model Training (Naïve Bayes) → 
5. Model Saving →  
6. Web App Integration (Flask) → 
7. Real-time Sentiment Prediction
