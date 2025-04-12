import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load your datasets (replace these paths with actual files)
diabetes_data = pd.read_csv('diabetes.csv')
cancer_data = pd.read_csv('cancer.csv')
heart_data = pd.read_csv('heart.csv')
parkinsons_data = pd.read_csv('parkinsons.csv')

# Preprocessing function
def preprocess_data(data, target_column):
    X = data.drop(columns=target_column, axis=1)
    Y = data[target_column]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

# Train and evaluate models
def train_models(X_train, X_test, Y_train, Y_test):
    models = {
        'SVM': SVC(kernel='linear'),
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Random Forest': RandomForestClassifier(n_estimators=100)
    }

    for name, model in models.items():
        model.fit(X_train, Y_train)
        predictions = model.predict(X_test)
        acc = accuracy_score(Y_test, predictions)
        print(f"{name} Accuracy: {acc:.2f}")

print("--- Diabetes Prediction ---")
X_train, X_test, Y_train, Y_test = preprocess_data(diabetes_data, 'Outcome')
train_models(X_train, X_test, Y_train, Y_test)

print("\n--- Cancer Prediction ---")
X_train, X_test, Y_train, Y_test = preprocess_data(cancer_data, 'diagnosis')
train_models(X_train, X_test, Y_train, Y_test)

print("\n--- Heart Disease Prediction ---")
X_train, X_test, Y_train, Y_test = preprocess_data(heart_data, 'target')
train_models(X_train, X_test, Y_train, Y_test)

print("\n--- Parkinson's Prediction ---")
X_train, X_test, Y_train, Y_test = preprocess_data(parkinsons_data, 'status')
train_models(X_train, X_test, Y_train, Y_test)

print("\nAll models trained successfully!")