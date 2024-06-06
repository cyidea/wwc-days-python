import pandas as pd

# Create a sample DataFrame
weather = pd.DataFrame({
    'city': ['New York', 'New York', 'New York', 'Chicago', 'Chicago', 'Chicago'],
    'day': ['Mon', 'Tue', 'Wed', 'Mon', 'Tue', 'Wed'],
    'temperature': [65, 70, 75, 60, 65, 70],
    'humidity': [60, 65, 70, 55, 60, 65]
})

print(weather)

# convert from a wide format to long format:
weather_long = weather.set_index(['city', 'day']).stack().reset_index()
weather_long.columns = ['city', 'day', 'type', 'value']
print('\n')
print(weather_long)