import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# again, you need to have these libs: pandas and scikit-learn

# Create the original dataframe
data = {'Temperature': [30, 32, 35, 20, 22, 25, 28],
        'Humidity': [60, 65, 70, 75, 80, 85, 90],
        'Pressure': [1010, 1012, 1015, 1008, 1006, 1003, 1000],
        'WindSpeed': [5, 6, 7, 4, 3, 2, 1],
        'Rainfall': [0, 0, 0, 1, 1, 1, 0],
        'Visibility': [10, 8, 9, 6, 7, 5, 10],
        'AQI': [20, 25, 30, 40, 35, 45, 50]}

df = pd.DataFrame(data)

# Separate features(X) and target(y) variables
X = df.drop('AQI', axis=1)
y = df['AQI']

# Split the data into training and testing datasets
# test_size is the percentage that will go into the test set, here is it 1/5
# random_state controls the selection of the data, 
# you need to provide an integer for random_state and stay with it.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# so since we used 0.2 for test_size, we should have 80% in the X_train

# Create and fit the Decision Tree Regressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)

# Predict on the training data
y_train_pred = regressor.predict(X_train)

# Calculate the Mean Absolute Error (MAE) for in-sample (training) data.
# Since we used these data for training, the MAE for this should be very small.
mae_train = mean_absolute_error(y_train, y_train_pred)

# Add predictions as a new column to the testing dataframe
# this is going to be useful when we print it out later for comparason
X_train['Predicted_AQI'] = y_train_pred

# the rest is going to deal with test dataset predictions:

# Predict on the testing data: 
y_test_pred = regressor.predict(X_test)

# Calculate the Mean Absolute Error (MAE) for out-of-sample (testing) data
mae_test = mean_absolute_error(y_test, y_test_pred)

# Add predictions as a new column to the testing dataframe
# this is going to be useful when we print it out later for comparason
X_test['Predicted_AQI'] = y_test_pred

print("Training Dataset and Corresponding Predicted Values:")
print(pd.concat([X_train, y_train], axis=1))

print("\nTesting Dataset and Corresponding Predicted Values:")
print(pd.concat([X_test, y_test], axis=1))

print("\nIn-sample MAE:", mae_train)
print("Out-of-sample MAE:", mae_test)

"""
result print out:

Training Dataset and Corresponding Predicted Values:
   Temperature  Humidity  Pressure  WindSpeed  Rainfall  Visibility  Predicted_AQI  AQI
5           25        85      1003          2         1           5           45.0   45
2           35        70      1015          7         0           9           30.0   30
4           22        80      1006          3         1           7           35.0   35
3           20        75      1008          4         1           6           40.0   40
6           28        90      1000          1         0          10           50.0   50

Testing Dataset and Corresponding Predicted Values:
   Temperature  Humidity  Pressure  WindSpeed  Rainfall  Visibility  Predicted_AQI  AQI
0           30        60      1010          5         0          10           30.0   20
1           32        65      1012          6         0           8           35.0   25

In-sample MAE: 0.0
Out-of-sample MAE: 10.0
"""