import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Load the ames_housing dataset and create the DataFrame
ames_housing = fetch_openml(name="house_prices", as_frame=True)
df = pd.DataFrame(ames_housing.data, columns=ames_housing.feature_names)
df['target'] = ames_housing.target

# Split the data into train and test sets
X = df.drop('target', axis=1)
y = df['target']

# try to prevent 'could not convert string to float ' error
# also to simply this example, we are going to just deal with numerical type
# so the following converts all non-numerical cells to numerical
# there are better ways to deal with it, we will do it in another code
X = X.apply(pd.to_numeric, errors='coerce')
y = y.apply(pd.to_numeric, errors='coerce')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# cleanup the data a little bit:
print('The columns that are missing all values: ')
cols_with_all_vals_missing = [col for col in X_train.columns
                     if X_train[col].isnull().all()]
# print(cols_with_all_vals_missing) # uncomment to see all the columns

# drop all these columns that have no value:
X_train = X_train.drop(cols_with_all_vals_missing, axis=1)
X_test = X_test.drop(cols_with_all_vals_missing, axis=1)


# To put the imputer into the pipeline:
numerical_transformer = SimpleImputer(strategy='median')
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, X_train.columns)
    ])

# Create a RandomForestRegressor with random_state=0
model = RandomForestRegressor(random_state=0)

# now instead of call the model.fit, we are going to create a pipeline to do it:
the_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', model)
    ])

# Fit the pipeline on the training data
the_pipeline.fit(X_train, y_train)

# Make predictions on the test data
y_pred = the_pipeline.predict(X_test)

# Calculate the MAE
mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)

"""
result:
MAE: 18174.82
"""