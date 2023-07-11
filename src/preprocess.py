import numpy as np
from sklearn.exceptions import NotFittedError
from sklearn.preprocessing import StandardScaler


class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.outlier_threshold = 3.0

    def remove_outliers(self, X):
        # Calculate the z-scores for each feature
        z_scores = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

        # Remove outliers based on the z-scores
        X_clean = X[(np.abs(z_scores) < self.outlier_threshold).all(axis=1)]
        return X_clean

    def preprocess_data(self, X):
        try:
            # Use the fitted scaler to transform the data
            X_scaled = self.scaler.transform(X)
            return X_scaled
        except NotFittedError:
            raise RuntimeError(
                "Scaler has not been fitted. Call fit() before preprocess_data()."
            )

    def fit(self, X):
        # Remove outliers
        X_clean = self.remove_outliers(X)

        # Fit the scaler
        self.scaler.fit(X_clean)

    def transform(self, X):
        # Remove outliers
        X_clean = self.remove_outliers(X)

        # Preprocess the data
        X_scaled = self.preprocess_data(X_clean)
        return X_scaled

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
