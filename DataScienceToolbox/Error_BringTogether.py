import pandas as pd
import os
cwd = os.getcwd()
print(cwd)
#df = pd.read_csv('/Users/David/Dropbox/Python3/git/Datacamp/DataScienceToolbox/tweets.csv')
tweets_df = pd.read_csv(cwd+'/DataScienceToolbox/tweets.csv')
print(tweets_df['text'])
# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2]=='RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)
