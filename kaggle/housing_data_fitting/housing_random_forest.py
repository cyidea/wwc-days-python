import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load the California Housing dataset and create the DataFrame
load_california = fetch_california_housing()
df = pd.DataFrame(load_california.data, columns=load_california.feature_names)
df['target'] = load_california.target

# Split the data into train and test sets
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a RandomForestRegressor with random_state=12
model = RandomForestRegressor(random_state=12)

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the MAE
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)

"""
result:
MAE: 0.326515
"""