import pandas as pd

data = [
    [1, 'Winston', 'winston@leetcode.com'],
    [2, 'Jonathan', 'jonathanisgreat'],
    [3, 'Annabelle', 'bella-@leetcode.com'],
    [4, 'Sally', 'sally.come@leetcode.com'],
    [5, 'Marwan', 'quarz#2020@leetcode.com'],
    [6, 'David', 'david69@gmail.com'],
    [7, 'Shapiro', '.shapo@leetcode.com']
]

columns = ['user_id', 'name', 'email']
users = pd.DataFrame(data, columns=columns)

print(users)

users = users.loc[users['email'].str.match(r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$')]

print(users)