

import nltk
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from imblearn.over_sampling import SMOTE  # For handling imbalanced data
import os  # Imported os for managing file paths
from sklearn.metrics import confusion_matrix


# Download necessary NLTK packages
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

# Load the dataset
df = pd.read_csv(r'C:\Users\tanis\OneDrive\Desktop\sentiment analysis project\data\YoutubeCommentsDataSet.csv')
print("Columns in dataset:", df.columns.tolist())

# Drop rows with missing 'Comment' or 'Sentiment' values
df.dropna(subset=['Comment', 'Sentiment'], inplace=True)

def clean_text(text):
    text = str(text)  # Ensure text is string
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters
    return text.strip().lower()  # Convert to lowercase

# Apply text cleaning to the comments
df['clean_text'] = df['Comment'].apply(clean_text)

# Initialize Lemmatizer
lemmatizer = WordNetLemmatizer()
df['lemmatized_tokens'] = df['clean_text'].apply(
    lambda x: [lemmatizer.lemmatize(word) for word in word_tokenize(x)]
)

# Vectorize the cleaned text
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), sublinear_tf=True, max_df=0.95, min_df=5)
X = vectorizer.fit_transform(df['clean_text'])  # Convert text to numerical features
y = df['Sentiment']  # Target variable

# Handle imbalanced data using SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Naive Bayes Model with Smoothing (alpha parameter)
model = MultinomialNB(alpha=1.0)  # Smoothing with alpha=1.0
model.fit(X_train, y_train)  # Train the model

# Make predictions
y_pred = model.predict(X_test)  # Make predictions

# Print accuracy and classification report
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)




# Ensure 'models' directory exists to save the model and vectorizer
if not os.path.exists('models'):
    os.makedirs('models')

# Save the trained model and vectorizer using pickle inside 'models' folder
with open(os.path.join("models", "sentiment_model.pkl"), "wb") as model_file:
    pickle.dump(model, model_file)

with open(os.path.join("models", "tfidf_vectorizer.pkl"), "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

# Function to load model and vectorizer for prediction from 'models' folder
def load_model():
    model_path = os.path.join("models", "sentiment_model.pkl")
    vectorizer_path = os.path.join("models", "tfidf_vectorizer.pkl")
    
    with open(model_path, "rb") as model_file:
        loaded_model = pickle.load(model_file)
    with open(vectorizer_path, "rb") as vectorizer_file:
        loaded_vectorizer = pickle.load(vectorizer_file)
    
    return loaded_model, loaded_vectorizer

# Apply the trained model to all comments and predict sentiment
df['predicted_sentiment'] = model.predict(X)  # Apply model to all comments

# Print a preview of comments and predicted sentiments
print(df[['Comment', 'Sentiment', 'predicted_sentiment']].head())

# Save the dataset with predictions to a CSV file
df.to_csv("YoutubeCommentsDataSet_with_predictions.csv", index=False)

# Function to predict sentiment of a new comment
def predict_sentiment(comment):
    model, vectorizer = load_model()
    clean_comment = clean_text(comment)
    vectorized_comment = vectorizer.transform([clean_comment])
    return model.predict(vectorized_comment)[0]

# Example comment for sentiment prediction
example_comment = "This video is amazing! I loved it."
print("Predicted Sentiment:", predict_sentiment(example_comment))
