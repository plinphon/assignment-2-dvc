import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    # Load train set
    train_dataset = pd.read_csv("data/train.csv")

    # Get X and Y
    y: np.ndarray = train_dataset.loc[:, "target"].values.astype("float32")
    X: np.ndarray = train_dataset.drop("target", axis=1).values

    # Create an instance of Logistic Regression Classifier and fit the data.
    clf = LogisticRegression(C=0.01, solver="lbfgs", max_iter=100)
    clf.fit(X, y)

    joblib.dump(clf, "models/model.joblib")
