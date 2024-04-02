import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# you would have installed both pandas and scikit-learn
# but if you haven't, here is how to install them on Mac:
# pip3 install --upgrade pip
# pip3 install pandas
# pip3 install scikit-learn

# Create a sample dataframe
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

# Create and fit the Decision Tree Regressor
regressor = DecisionTreeRegressor()
regressor.fit(X, y)

# Make predictions
new_data = {'Temperature': [27, 29],
            'Humidity': [70, 75],
            'Pressure': [1013, 1011],
            'WindSpeed': [3, 4],
            'Rainfall': [0, 1],
            'Visibility': [8, 7]}
new_df = pd.DataFrame(new_data)

# Predict on new data
predictions = regressor.predict(new_df)

# Add predictions as a new column to the new_df
new_df['Predicted_AQI'] = predictions

# Concatenate new_df with the original dataframe df
df_with_predictions = pd.concat([df, new_df], ignore_index=True)

print(df_with_predictions)