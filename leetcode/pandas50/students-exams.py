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

print("Students DataFrame:")
print(students)
print("\nSubjects DataFrame:")
print(subjects)
print("\nExaminations DataFrame:")
print(examinations)


# result = employees.merge(right=employeeUNI, left_on="id", right_on="employee_id", how="left")
# print(result[['unique_id', 'name']])

# result = examinations.groupby(['student_id','subject_name']).size().reset_index(name='count')

result = examinations.groupby(['student_id','subject_name']).size().reset_index(name='attended_exams')

merged = result.merge(right=students, on='student_id', how='outer').sort_values(by=['student_id', 'subject_name'])

print(merged)

