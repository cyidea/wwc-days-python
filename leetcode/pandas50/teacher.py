import pandas as pd

data = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 3, 3],
    [2, 1, 1],
    [2, 2, 1],
    [2, 3, 1],
    [2, 4, 1]
]

columns = ['teacher_id', 'subject_id', 'dept_id']
teacher = pd.DataFrame(data, columns=columns)

print(teacher)

print('\n')

thes = teacher.groupby(['teacher_id']).subject_id.unique()
newdf = thes.to_frame().reset_index()
newdf['cnt'] = newdf.apply(lambda row: len(row['subject_id']), axis=1)
print(newdf[['teacher_id', 'cnt']])
# print(thes.to_frame().reset_index().rename(columns={'event_date':'first_login'}))
