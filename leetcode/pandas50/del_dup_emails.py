import pandas as pd

data = [
    [2, 'john@example.com'],
    [3, 'bob@example.com'],
    [1, 'john@example.com']
]

columns = ['id', 'email']
person = pd.DataFrame(data, columns=columns)

# delete duplicate emails
print(person)
print('\n')

# sort the person df by email then by id asc
person.sort_values(by=['email', 'id'], ascending=True, inplace=True)
print('\naftersort:')
print(person)

person.drop_duplicates(subset=['email'], keep='first', inplace=True)
print(person)