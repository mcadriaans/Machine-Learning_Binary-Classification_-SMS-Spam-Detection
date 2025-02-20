
import joblib
import numpy as np
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

# ℹ️ Load Model, Vectorizer, and Scaler
loaded_model = joblib.load('svc_spam_classifier.pkl')
loaded_vectorizer = joblib.load('tfidf_vectorizer.pkl')
loaded_scaler = joblib.load('minmax_scaler.pkl')  # Load the scaler used in training

# ℹ️ Function to Extract Additional Features
def extract_features(text):
    character_count = len(text)
    sentence_count = text.count('.') + text.count('!') + text.count('?')  # Simple sentence count
    return np.array([[character_count, sentence_count]])

# ℹ️ Function to Preprocess Text (Replace this with your actual text preprocessing function)
def text_preprocessing(text):
  stop_words = set(stopwords.words('english'))
  stemmer = PorterStemmer()

  words = word_tokenize(text)
  cleaned_words = [stemmer.stem(word) for word in words if word.isalnum() and word.lower() not in stop_words]
  return ' '.join(cleaned_words)

# ℹ️ Prompt the user to enter a new message
new_message = input("Enter a new message: ")

# ℹ️ Preprocess the new message
new_message_cleaned = text_preprocessing(new_message)  # Apply same text cleaning

# ℹ️ Transform text using the saved TF-IDF vectorizer
new_message_tfidf = loaded_vectorizer.transform([new_message_cleaned]).toarray()

# ℹ️ Extract additional features and scale them using the saved MinMaxScaler
new_message_features = extract_features(new_message)
new_message_features_scaled = loaded_scaler.transform(new_message_features)

# ℹ️ Combine TF-IDF and Additional Features (Ensure 3002 features)
new_message_combined = np.hstack((new_message_tfidf, new_message_features_scaled))

# ℹ️ Predict using the trained model
prediction = loaded_model.predict(new_message_combined)
print('Spam' if prediction[0] == 1 else 'Ham')
