import os
import pandas as pd
cwd = os.getcwd()
df=cwd+'/DataScienceToolbox2/tweets.csv'
df=pd.read_csv(df)

# Extract the created_at column from df: tweet_time
tweet_time = df['created_at']

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']

# Print the extracted times
print(tweet_clock_time)
