import pandas as pd

data = [
    [1, '2020-11-28', 4, 32],
    [1, '2020-11-28', 55, 200],
    [1, '2020-12-3', 1, 42],
    [2, '2020-11-28', 3, 33],
    [2, '2020-12-9', 47, 74]
]

columns = ['emp_id', 'event_day', 'in_time', 'out_time']
attendance = pd.DataFrame(data, columns=columns)

print(attendance)

print('\n')

attendance['diff'] = attendance.apply(lambda row: row['out_time'] - row['in_time'], axis=1)
print(attendance)

thesum = attendance.groupby(['emp_id', 'event_day']).sum()

df = thesum.reset_index()
print(df)

df.rename(columns={'event_day':'day', 'diff': 'total_time'}, inplace=True)
print(df[['day', 'emp_id', 'total_time']])