import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.lower().str.capitalize()
    return users.sort_values(by='user_id')

# Create the data as a list of lists
data = [[1, 'aLice ann'], [2, 'bOB']]

# Create the column names
columns = ['user_id', 'name']

# Create the DataFrame
users = pd.DataFrame(data, columns=columns)

print(users)

print(fix_names(users))