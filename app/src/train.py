import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import joblib

def load_data(path: str):
    return pd.read_excel(path)

def prepare_data(data):
    X = data.drop(columns="Class")
    y = data["Class"]

    encoder = LabelEncoder()
    y = encoder.fit_transform(y)

    return X, y, encoder


def split_data(X, y):
    return train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )


def train_model(X_train, y_train):

    parameters = {
        "n_estimators": [50, 100, 200, 300],
        "max_depth": [3, 5, 10, None],
        "min_samples_split": [2, 4, 6],
        "min_samples_leaf": [1, 2, 4],
    }

    rf = RandomForestClassifier(random_state=42)

    search = RandomizedSearchCV(
        estimator=rf,
        param_distributions=parameters,
        n_iter=20,
        cv=5,
        scoring="accuracy",
        random_state=42,
    )

    search.fit(X_train, y_train)

    return search.best_estimator_


def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    print("Accuracy:")
    print(accuracy_score(y_test, predictions))

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))


def main():
    data = load_data("/home/vorob/projects/Python_projects/Seed_prediction/app/data/Pumpkin_Seeds_Dataset.xlsx")

    X, y, encoder = prepare_data(data)

    X_train, X_test, y_train, y_test = split_data(X, y)

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)

    joblib.dump(model, "model.joblib")

    joblib.dump(encoder, "label_encoder.joblib")


if __name__ == "__main__":
    main()