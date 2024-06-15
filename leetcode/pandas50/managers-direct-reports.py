import pandas as pd

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

print(employees)

counts = employees.groupby(['managerId']).id.agg(
    num_times = "count"
     ).reset_index()
newq = counts.query('num_times >= 5')
newq = newq.merge(employees, left_on='managerId', right_on='id', how='left')
print(newq[['name']])


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
employee = pd.DataFrame(data, columns=columns)

print(employee)

counts = employee.groupby(['managerId']).id.agg(
    num_times = "count"
     ).reset_index()
newq = counts.query('num_times >= 5')
newq = newq.merge(employee, left_on='managerId', right_on='id', how='left')
print(newq[['name']].dropna())

# need to fix the third error
# using https://stackoverflow.com/questions/53198369/conditional-dropna-pandas
# because looks like 'null' and na is the same,
# but we have to get rid of only na.
# anyway, copy the example here and deal with.
