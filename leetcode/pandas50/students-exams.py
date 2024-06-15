import pandas as pd

# Students DataFrame
students_data = [
    [1, 'Alice'],
    [2, 'Bob'],
    [13, 'John'],
    [6, 'Alex']
]
students = pd.DataFrame(students_data, columns=['student_id', 'student_name'])

# Subjects DataFrame
subjects_data = [
    ['Math'],
    ['Physics'],
    ['Programming']
]
subjects = pd.DataFrame(subjects_data, columns=['subject_name'])

# Creating a cartesian product dataframe between student_id and subject_name
student_id_list = students['student_id']
subject_name_list = subjects['subject_name']

newindex = pd.MultiIndex.from_product([student_id_list, subject_name_list], 
                                   names = ["student_id", "subject_name"])

allrows = pd.DataFrame(index = newindex).reset_index()
print(allrows)

'''
    student_id subject_name
0            1         Math
1            1      Physics
2            1  Programming
3            2         Math
4            2      Physics
5            2  Programming
6           13         Math
7           13      Physics
8           13  Programming
9            6         Math
10           6      Physics
11           6  Programming
'''



# Examinations DataFrame
examinations_data = [
    [1, 'Math'],
    [1, 'Physics'],
    [1, 'Programming'],
    [2, 'Programming'],
    [1, 'Physics'],
    [1, 'Math'],
    [13, 'Math'],
    [13, 'Programming'],
    [13, 'Physics'],
    [2, 'Math'],
    [1, 'Math']
]
examinations = pd.DataFrame(examinations_data, columns=['student_id', 'subject_name'])

result = examinations.groupby(['student_id','subject_name']).size().reset_index(name='attended_exams')

print('\n')
print(result)
print('\n')
print('final result: ')
merged = result.merge(right=allrows, on=['student_id', 'subject_name'], how='right').sort_values(by=['student_id', 'subject_name']).fillna(0)
merged = merged.merge(right=students, on='student_id', how='left')

print(merged[['student_id', 'student_name', 'subject_name', 'attended_exams']])


