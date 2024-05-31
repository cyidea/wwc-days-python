import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    columns=['tweet_id']
    retval = tweets[tweets.apply(lambda row: len(row['content']) > 15 , axis=1)]
    if retval.empty:
        return pd.DataFrame(columns=columns)
    else:
        return retval[columns]

data = [
    [1, 'Vote for Biden'],
    [2, 'Let us make America great again!']
]

columns = ['tweet_id', 'content']
tweets = pd.DataFrame(data, columns=columns)

print(tweets)

print(invalid_tweets(tweets))