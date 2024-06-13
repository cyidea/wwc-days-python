import pandas as pd

data = [
    [1, 'Alice'],
    [7, 'Bob'],
    [11, 'Meir'],
    [90, 'Winston'],
    [3, 'Jonathan']
]

employees = pd.DataFrame(data, columns=['id', 'name'])

print(employees)

data = [
    [3, 1],
    [11, 2],
    [90, 3]
]

employeeUNI = pd.DataFrame(data, columns=['employee_id', 'unique_id'])

print(employeeUNI)

# counts = actorDirector.groupby(['actor_id', 'director_id']).timestamp.agg(
#     num_times = "count"
#      ).reset_index()
# newq = counts.query('num_times >= 3')[['actor_id', 'director_id']]
# print(newq)

result = employees.merge(right=employeeUNI, left_on="id", right_on="employee_id", how="left")
print(result[['unique_id', 'name']])