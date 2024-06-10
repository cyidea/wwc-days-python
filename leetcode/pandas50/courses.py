import pandas as pd

data = [
    ['A', 'Math'],
    ['B', 'English'],
    ['C', 'Math'],
    ['D', 'Biology'],
    ['E', 'Math'],
    ['F', 'Computer'],
    ['G', 'Math'],
    ['H', 'Math'],
    ['I', 'Math']
]

columns = ['student', 'class']
courses = pd.DataFrame(data, columns=columns)

print(courses)

print('\n')

thes = courses.groupby(['class']).student.count()
newdf = thes.to_frame().reset_index()
newdff = newdf[newdf['student'] >= 5]
print(newdff[['class']])
