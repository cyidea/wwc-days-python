import pandas as pd

data = [
    [1, 2, '2016-03-01', 5],
    [1, 2, '2016-05-02', 6],
    [2, 3, '2017-06-25', 1],
    [3, 1, '2016-03-02', 0],
    [3, 4, '2018-07-03', 5]
]

columns = ['player_id', 'device_id', 'event_date', 'games_played']
activity = pd.DataFrame(data, columns=columns)

print(activity)

print('\n')

# attendance['diff'] = attendance.apply(lambda row: row['out_time'] - row['in_time'], axis=1)
# print(attendance)

thes = activity.groupby(['player_id']).event_date.min()


print(thes.to_frame().reset_index().rename(columns={'event_date':'first_login'}))

# df.rename(columns={'event_day':'day', 'diff': 'total_time'}, inplace=True)
# print(df[['day', 'emp_id', 'total_time']])