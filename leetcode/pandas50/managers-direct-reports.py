import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    print(employee)
    if employee.empty:
        return pd.DataFrame({'name': []})
        
    counts = employee.groupby(['managerId']).id.agg(
        num_times = "count"
        ).reset_index()
    newq = counts.query('num_times >= 5')
    newq = newq.merge(employee, left_on='managerId', right_on='id', how='left')
    print('\n')
    print(newq)
    newqnameempty = newq[~(newq['name'].isna())]
    newqidempty = newq[~(newq['id'].isna())]
    if newqidempty.empty:
        return pd.DataFrame({'name': []})

    if newqnameempty.empty:
        return pd.DataFrame({'name': [None]})
    else:
        return newqnameempty[['name']]

# first test:
data = [
    [101, 'John', 'A', None],
    [102, 'Dan', 'A', 101],
    [103, 'James', 'A', 101],
    [104, 'Amy', 'A', 101],
    [105, 'Anne', 'A', 101],
    [106, 'Ron', 'B', 101]
]

columns = ['id', 'name', 'department', 'managerId']
employees = pd.DataFrame(data, columns=columns)

print(find_managers(employees))

############ this is a failed case, going to debug this:
data = [
    [101, 'John', 'A', None],
    [102, 'Dan', 'A', 100],
    [103, 'James', 'A', 100],
    [104, 'Amy', 'A', 100],
    [105, 'Anne', 'A', 100],
    [106, 'Ron', 'B', 100]
]

columns = ['id', 'name', 'department', 'managerId']
employees = pd.DataFrame(data, columns=columns)

print(find_managers(employees))

# 3rd case:
data = [
    [101, None, 'A', None],
    [102, None, 'A', 101],
    [103, None, 'A', 101],
    [104, None, 'A', 101],
    [105, None, 'A', 101],
    [106, None, 'B', 101]
]

columns = ['id', 'name', 'department', 'managerId']
employees = pd.DataFrame(data, columns=columns)
print(find_managers(employees))

