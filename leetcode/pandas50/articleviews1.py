import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df1 = views[views['author_id'] == views['viewer_id']]
    df2 = df1['author_id']
    df2 = pd.DataFrame({'id': df2}).drop_duplicates().sort_values(by='id', ascending=True)
    return df2

data = [
    [1, 3, 5, '2019-08-01'],
    [1, 3, 6, '2019-08-02'],
    [2, 7, 7, '2019-08-01'],
    [2, 7, 6, '2019-08-02'],
    [4, 7, 1, '2019-07-22'],
    [3, 4, 4, '2019-07-21'],
    [3, 4, 4, '2019-07-21']
]

columns = ['article_id', 'author_id', 'viewer_id', 'view_date']
views = pd.DataFrame(data, columns=columns)

# Convert the 'view_date' column to datetime
views['view_date'] = pd.to_datetime(views['view_date'])

mydf = article_views(views)
print(mydf)