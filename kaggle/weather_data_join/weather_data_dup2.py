import pandas as pd

# US city Toronto, Kansas and Canada city Toronto, Ontario has the same name.
# 
# Create the US weather DataFrame
us_data = {'City': ['Toronto', 'Los Angeles', 'Chicago'],
           'Temperature (C)': [30, 25, 10]}
df_us = pd.DataFrame(us_data)

# Create the Canada weather DataFrame
canada_data = {'City': ['Toronto', 'Vancouver', 'Montreal'],
               'Temperature (C)': [12, 18, 8]}
df_canada = pd.DataFrame(canada_data)


df_combined = df_us.join(df_canada.set_index('City'), on='City', lsuffix='_US', rsuffix='_CAN', how='inner')
print(df_combined)

"""
result: this is the most strict join
      City  Temperature (C)_US  Temperature (C)_CAN
0  Toronto                  30                   12
"""

df_combined = df_us.join(df_canada.set_index('City'), on='City', lsuffix='_US', rsuffix='_CAN', how='left')
print(df_combined)

"""
result: this has everything on the 'left' dataset, in this case is 'US'

         City  Temperature (C)_US  Temperature (C)_CAN
0      Toronto                  30                 12.0
1  Los Angeles                  25                  NaN
2      Chicago                  10                  NaN
"""

df_combined = df_us.join(df_canada.set_index('City'), on='City', lsuffix='_US', rsuffix='_CAN', how='right')
print(df_combined)
"""
result: this has everything on the 'right' dataset, in this case is 'CANADA'
        City  Temperature (C)_US  Temperature (C)_CAN
0.0    Toronto                30.0                   12
NaN  Vancouver                 NaN                   18
NaN   Montreal                 NaN                    8
"""

df_combined = df_us.join(df_canada.set_index('City'), on='City', lsuffix='_US', rsuffix='_CAN', how='outer')
print(df_combined)
"""
result: this joins every row based on the city name
            City  Temperature (C)_US  Temperature (C)_CAN
2.0      Chicago                10.0                  NaN
1.0  Los Angeles                25.0                  NaN
NaN     Montreal                 NaN                  8.0
0.0      Toronto                30.0                 12.0
NaN    Vancouver                 NaN                 18.0

"""

