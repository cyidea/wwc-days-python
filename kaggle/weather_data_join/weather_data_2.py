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

# set the index on both dataFrames to use the temperature column
df_us.set_index(['Temperature (C)'], inplace=True)
df_canada.set_index(['Temperature (C)'], inplace=True)

df_combined = df_us.join(df_canada, lsuffix='_US', rsuffix='_CAN', how='outer')
print(df_combined)

"""
result:
                     City_US   City_CAN
Temperature (C)                        
8                        NaN   Montreal
10                   Chicago        NaN
12                       NaN    Toronto
18                       NaN  Vancouver
25               Los Angeles        NaN
30                   Toronto        NaN
"""

# Find the cities in df_us that don't exist in df_canada
cities_not_in_canada = df_us[~df_us['City'].isin(df_canada['City'])]

print("Cities in df_us that don't exist in df_canada:")
print(cities_not_in_canada)


