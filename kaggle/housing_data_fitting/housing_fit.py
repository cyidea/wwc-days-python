import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# Load the load_california Housing dataset
# and create the DataFrame using some boilerplate code:
load_california = fetch_california_housing()
df = pd.DataFrame(load_california.data, columns=load_california.feature_names)
df['target'] = load_california.target

# take a look at the printout & get yourself familiar with the data a little
print(df.head())

"""
this prints: ( I guess the target is in millions, California is expensive!)
   MedInc  HouseAge  AveRooms  AveBedrms  Population  AveOccup  Latitude  Longitude  target
0  8.3252      41.0  6.984127   1.023810       322.0  2.555556     37.88    -122.23   4.526
1  8.3014      21.0  6.238137   0.971880      2401.0  2.109842     37.86    -122.22   3.585
2  7.2574      52.0  8.288136   1.073446       496.0  2.802260     37.85    -122.24   3.521
3  5.6431      52.0  5.817352   1.073059       558.0  2.547945     37.85    -122.25   3.413
4  3.8462      52.0  6.281853   1.081081       565.0  2.181467     37.85    -122.25   3.422
"""

# Split the data into train and test sets
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a function to train and evaluate the model with different max_leaf_nodes
def evaluate_model(max_leaf_nodes):
    # Create a Decision Tree Regressor with specified max_leaf_nodes
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=42)
    
    # Fit the model on the training data
    model.fit(X_train, y_train)
    
    # Make predictions on the test data
    y_pred = model.predict(X_test)
    
    # Calculate the MAE
    mae = mean_absolute_error(y_test, y_pred)
    return mae

# Test different max_leaf_nodes values
max_leaf_nodes_values = [100, 200, 300, 500, 700, 900]
mae_results = []

for max_leaf_nodes in max_leaf_nodes_values:
    # Evaluate the model and get the MAE
    mae = evaluate_model(max_leaf_nodes)
    mae_results.append(mae)

# Create a DataFrame to store the results
results_df = pd.DataFrame({'max_leaf_nodes': max_leaf_nodes_values, 'MAE': mae_results})

# Print the results
print(results_df)

"""
result: (from the result looks like max_leaf_nodes 500 gives the lowest MAE)
   max_leaf_nodes       MAE
0             100  0.448238
1             200  0.435153
2             300  0.428011
3             500  0.418090
4             700  0.419268
5             900  0.419411
"""