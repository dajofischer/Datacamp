# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
import os
cwd = os.getcwd()
#df = pd.read_csv('/Users/David/Dropbox/Python3/git/Datacamp/DataScienceToolbox/tweets.csv')
df = pd.read_csv(cwd+'/DataScienceToolbox/tweets.csv')
#df = pd.read_csv('tweets.csv')
#print(df)
# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        #langs_count[entry]=langs_count[entry]+1
        langs_count[entry] +=1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)
