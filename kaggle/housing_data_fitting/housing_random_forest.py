import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer

# Load the ames_housing dataset and create the DataFrame
ames_housing = fetch_openml(name="house_prices", as_frame=True)
df = pd.DataFrame(ames_housing.data, columns=ames_housing.feature_names)
df['target'] = ames_housing.target

# Split the data into train and test sets
X = df.drop('target', axis=1)
y = df['target']

# try to prevent 'could not convert string to float' error.
# the error occurs if there are string type values in the dataset
X = X.apply(pd.to_numeric, errors='coerce')
y = y.apply(pd.to_numeric, errors='coerce')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# At this point if you are in the debugger you can inspect these values:
# X.shape[0] # which gives the number of rows for the original dataframe
# X_train.shape[0] # gives the number of rows for the training set
# X_test.shape[0] # gives the number of rows for the test set
# in general .shape gives you the number of rows and number of columns of a dataframe


# Create a RandomForestRegressor with random_state=0
model = RandomForestRegressor(random_state=0)

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the MAE
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)

"""
result:
MAE: 18316.85
"""

# next we are going to get rid of the missing values
# we first will deal with columns that have all columns missing
# then we will 'Impute' the missing values with the 'median' of available values

print('The columns that are missing all values: ')
cols_with_all_vals_missing = [col for col in X_train.columns
                     if X_train[col].isnull().all()]
print(cols_with_all_vals_missing)
"""
Print out: Here are the columns we will drop:
['MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 
'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 
'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'ExterQual', 
'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 
'BsmtFinType2', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual', 
'Functional', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 
'PavedDrive', 'PoolQC', 'Fence', 'MiscFeature', 'SaleType', 'SaleCondition']
"""

# drop all these columns that have no value:
X_train = X_train.drop(cols_with_all_vals_missing, axis=1)
X_test = X_test.drop(cols_with_all_vals_missing, axis=1)

# and we will use SimpleImputer that can deal with columns that have
# both null values and non-null values
# it will fill the null values with the median of existing values
my_imputer = SimpleImputer(strategy='median')
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_test = pd.DataFrame(my_imputer.transform(X_test))

# imputation removed column names; put them back
imputed_X_train.columns = X_train.columns
imputed_X_test.columns = X_test.columns

# Create a RandomForestRegressor with random_state=0
model = RandomForestRegressor(random_state=0)

# Fit the model on the modified (imputed) training data
model.fit(imputed_X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(imputed_X_test)

# Calculate the MAE
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)

"""
result:
MAE: 18174.82
"""