import pandas as pd

# US city Toronto, Kansas and Canada city Toronto, Ontario has the same name.
# One ways to do it is to create a new column to separate the data by 'Country'
# 
# Create the US weather DataFrame
us_data = {'City': ['Toronto', 'Los Angeles', 'Chicago'],
           'Temperature (C)': [30, 25, 10],
           'Country': ['US', 'US', 'US']}
df_us = pd.DataFrame(us_data)

# Create the Canada weather DataFrame
canada_data = {'City': ['Toronto', 'Vancouver', 'Montreal'],
               'Temperature (C)': [12, 18, 8],
               'Country': ['Canada', 'Canada', 'Canada']}
df_canada = pd.DataFrame(canada_data)

# Create the Europe weather DataFrame
europe_data = {'City': ['London', 'Paris', 'Berlin'],
               'Temperature (C)': [9, 14, 7],
               'Country': ['Europe', 'Europe', 'Europe']}
df_europe = pd.DataFrame(europe_data)

# Concatenate the DataFrames vertically
df_combined = pd.concat([df_us, df_canada, df_europe])

# Reset the index
df_combined = df_combined.reset_index(drop=True)

# Display the combined DataFrame
print(df_combined)

"""
result:
          City  Temperature (C) Country
0      Toronto               30      US
1  Los Angeles               25      US
2      Chicago               10      US
3      Toronto               12  Canada
4    Vancouver               18  Canada
5     Montreal                8  Canada
6       London                9  Europe
7        Paris               14  Europe
8       Berlin                7  Europe

"""

df_combined = df_us.join(df_canada.set_index('City'), on='City', lsuffix='_US', rsuffix='_CAN', how='inner')
print(df_combined)

"""

"""

df_combined = df_us.join(df_canada.set_index('City'), on='City', lsuffix='_US', rsuffix='_CAN', how='left')
print(df_combined)

"""
result:

"""

df_combined = df_us.join(df_canada.set_index('City'), on='City', lsuffix='_US', rsuffix='_CAN', how='right')
print(df_combined)
"""
result:

"""

df_combined = df_us.join(df_canada.set_index('City'), on='City', lsuffix='_US', rsuffix='_CAN', how='outer')
print(df_combined)
"""
result:

"""

