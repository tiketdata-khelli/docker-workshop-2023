from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from src.preprocess import DataPreprocessor

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

print("X shape:", X.shape)
print("y shape:", y.shape)
print("features:", iris.feature_names)
print("Classes:", iris.target_names)
print("--------------------\n")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Preprocess the data
preprocessor = DataPreprocessor()
X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)

# Train the decision tree classifier
classifier = DecisionTreeClassifier()
print("Training the classifier...")
classifier.fit(X_train, y_train)
print("Classifier trained!\n")

# Predict on the test set
print("--------------------")
print("Predicting on the test set...")
y_pred = classifier.predict(X_test)
print("Predictions completed!\n")

# Evaluate the classifier
print(classification_report(y_test, y_pred))
