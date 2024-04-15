import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# you would have to have both pandas and scikit-learn
# but if you don't, here is how to install them on Mac:
# pip3 install --upgrade pip
# pip3 install pandas
# pip3 install scikit-learn
# use kaggle's medium dataset
# https://www.kaggle.com/datasets/dorianlazar/medium-articles-dataset
# download the csv file from here
# store it locally, in the same directory as the code in fact
# I kept the medium_data.csv

# Create the dataframe that contain historical medium data
df = pd.read_csv('medium_data.csv')

print(df.columns)

# these are the columns:
"""
['id', 'url', 'title', 'subtitle', 'image', 'claps', 'responses',
       'reading_time', 'publication', 'date']
"""

# but we are only concerned with these columns:
features = ['id', 'title', 'subtitle', 'claps', 'responses', 'reading_time', 'publication', 'date']

print(df[features].head())

""""
The data looks like:
   id                                              title                                 subtitle  claps responses  reading_time           publication        date
0   1  A Beginner’s Guide to Word Embedding with Gens...                                      NaN    850         8             8  Towards Data Science  2019-05-30
1   2  Hands-on Graph Neural Networks with PyTorch & ...                                      NaN   1100        11             9  Towards Data Science  2019-05-30
2   3                       How to Use ggplot2 in Python         A Grammar of Graphics for Python    767         1             5  Towards Data Science  2019-05-30
3   4  Databricks: How to Save Files in CSV on Your L...  When I work on Python projects dealing…    354         0             4  Towards Data Science  2019-05-30
4   5  A Step-by-Step Implementation of Gradient Desc...          One example of building neural…    211         3             4  Towards Data Science  2019-05-30

"""

"""
questions I would like to ask:
which publication has the most claps, and the most number of articles that got claps.
what is the reading_time relationship with the claps
whether having a subtitle affects the claps.
if the date falling on a weekend, friday, or days of the week affect the claps
not knowing what the 'responses' means I can't tell how to use the responses. until I figure that out

"""