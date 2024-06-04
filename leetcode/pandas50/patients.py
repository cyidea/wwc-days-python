import pandas as pd

data = [
    [1, 'Daniel', 'YFEV COUGH'],
    [2, 'Alice', ''],
    [3, 'Bob', 'DIAB100 MYOP'],
    [4, 'George', 'ACNE DIAB100'],
    [5, 'Alain', 'DIAB201']
]

columns = ['patient_id', 'patient_name', 'conditions']
patients = pd.DataFrame(data, columns=columns)

print(patients)

patients = patients.loc[patients['conditions'].str.match(r'(^DIAB1)|.*\s+DIAB1')]

print('\n')
print(patients)