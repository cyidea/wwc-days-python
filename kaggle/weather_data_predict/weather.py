import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# you would have to have both pandas and scikit-learn
# but if you don't, here is how to install them on Mac:
# pip3 install --upgrade pip
# pip3 install pandas
# pip3 install scikit-learn

# Create the dataframe that contain historical weather data
data = {'Temperature': [30, 32, 35, 20, 22, 25, 28],
        'Humidity': [60, 65, 70, 75, 80, 85, 90],
        'Pressure': [1010, 1012, 1015, 1008, 1006, 1003, 1000],
        'WindSpeed': [5, 6, 7, 4, 3, 2, 1],
        'Rainfall': [0, 0, 0, 1, 1, 1, 0],
        'Visibility': [10, 8, 9, 6, 7, 5, 10],
        'AQI': [20, 25, 30, 40, 35, 45, 50]}

# create a Pandas DataFrame using the data
df = pd.DataFrame(data)

# Separate features(X) and target(y) variables
# We are singling out the AQI (air quality index)
# because we want to predict AQI
X = df.drop('AQI', axis=1)
y = df['AQI']

# Create and fit the Decision Tree Regressor
regressor = DecisionTreeRegressor()
regressor.fit(X, y)

# from this time on we can use the regressor 
# for making predictions:

# Make predictions on new data
new_data = {'Temperature': [27, 29],
            'Humidity': [70, 75],
            'Pressure': [1013, 1011],
            'WindSpeed': [3, 4],
            'Rainfall': [0, 1],
            'Visibility': [8, 7]}
new_df = pd.DataFrame(new_data)

# Predict on new data and store the result in 'predictions'
predictions = regressor.predict(new_df)

# Add predictions as a new column to the new_df
new_df['Predicted_AQI'] = predictions

# Concatenate new_df with the original dataframe df
# this is just one way to use the prediction.
df_with_predictions = pd.concat([df, new_df], ignore_index=True)

print(df_with_predictions)

"""
result: As you can see the predicted_AQI shows only for the two new data rows
   Temperature  Humidity  Pressure  WindSpeed  Rainfall  Visibility   AQI  Predicted_AQI
0           30        60      1010          5         0          10  20.0            NaN
1           32        65      1012          6         0           8  25.0            NaN
2           35        70      1015          7         0           9  30.0            NaN
3           20        75      1008          4         1           6  40.0            NaN
4           22        80      1006          3         1           7  35.0            NaN
5           25        85      1003          2         1           5  45.0            NaN
6           28        90      1000          1         0          10  50.0            NaN
7           27        70      1013          3         0           8   NaN           25.0
8           29        75      1011          4         1           7   NaN           35.0

"""