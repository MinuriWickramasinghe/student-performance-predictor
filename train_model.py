import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Load dataset
data = pd.read_csv("data/student-mat.csv", sep=";")


# Create performance category
def performance(mark):
    if mark >= 14:
        return "Good"
    elif mark >= 10:
        return "Average"
    else:
        return "Poor"


data["performance"] = data["G3"].apply(performance)


# Features
X = data[["studytime", "failures", "absences", "G1", "G2"]]

# Target
y = data["performance"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = RandomForestClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

print("Model trained successfully!")


# Predictions
predictions = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)


# Classification report
print("\nClassification Report:")
print(classification_report(y_test, predictions))


# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))


# Save model
with open("model/student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved successfully!")