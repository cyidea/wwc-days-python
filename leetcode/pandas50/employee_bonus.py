import pandas as pd

def cal_bonus(row):

    bonus = 0
    if row['employee_id']%2 == 1 and not row['starts_with_M']:
        bonus = row['salary']
    
        
    return bonus

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['starts_with_M'] = employees['name'].str.startswith('M')

    employees['bonus'] = employees.apply(cal_bonus, axis=1)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)

data = [
    [2, 'Meir', 3000],
    [3, 'Michael', 3800],
    [7, 'Addilyn', 7400],
    [8, 'Juan', 6100],
    [9, 'Kannon', 7700]
]

columns = ['employee_id', 'name', 'salary']
employees = pd.DataFrame(data, columns=columns)

print(employees)

# keeping only three columns (to demonstrate keeping specific columns):
print(calculate_special_bonus(employees))
