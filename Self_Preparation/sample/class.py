import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Data Preparation
# Sample data (replace with your actual data)
data = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [2, 4, 5, 4, 5],
    'target': [2.1, 4.2, 5.3, 4.1, 5.2]
}
df = pd.DataFrame(data)

# Split data into features (X) and target (y)
X = df[['feature1', 'feature2']]
y = df['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Model Training
# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Model Evaluation
# Evaluate the model on the test set
score = model.score(X_test, y_test)
print(f"Model Score (R^2): {score}")

# 4. Making Predictions
# Example prediction
new_data = pd.DataFrame({'feature1': [6], 'feature2': [7]})
prediction = model.predict(new_data)
print(f"Prediction for new data: {prediction}")


