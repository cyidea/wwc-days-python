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