import pandas as pd

# Create the US weather DataFrame
us_data = {'City': ['New York', 'Los Angeles', 'Chicago'],
           'Temperature (C)': [15, 25, 10]}
df_us = pd.DataFrame(us_data)

# Create the Canada weather DataFrame
canada_data = {'City': ['Toronto', 'Vancouver', 'Montreal'],
               'Temperature (C)': [12, 18, 8]}
df_canada = pd.DataFrame(canada_data)

# Create the Europe weather DataFrame
europe_data = {'City': ['London', 'Paris', 'Berlin'],
               'Temperature (C)': [9, 14, 7]}
df_europe = pd.DataFrame(europe_data)

# Concatenate the DataFrames vertically
df_combined = pd.concat([df_us, df_canada, df_europe])

# Reset the index
df_combined = df_combined.reset_index(drop=True)

# Display the combined DataFrame
print(df_combined)

"""
result:
          City  Temperature (C)
0     New York               15
1  Los Angeles               25
2      Chicago               10
3      Toronto               12
4    Vancouver               18
5     Montreal                8
6       London                9
7        Paris               14
8       Berlin                7
"""

# another way to look at it, if we want to index on the 'City' column:
df_us = df_us.set_index(['City'])
df_canada = df_canada.set_index(['City'])
df_europe = df_europe.set_index(['City'])
df_combined = pd.concat([df_us, df_canada, df_europe])
print(df_combined)
"""
result:
             Temperature (C)
City                        
New York                  15
Los Angeles               25
Chicago                   10
Toronto                   12
Vancouver                 18
Montreal                   8
London                     9
Paris                     14
Berlin                     7
"""
