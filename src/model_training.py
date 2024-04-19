# src/model_training.py
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import pickle

def train_model(documents, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(documents)
    y = labels
    model = SVC()
    model.fit(X, y)
    return model, vectorizer

def save_model(model, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(model, file)
