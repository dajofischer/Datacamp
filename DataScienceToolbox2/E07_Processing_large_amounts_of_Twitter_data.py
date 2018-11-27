import os
import pandas as pd
cwd = os.getcwd()
print(cwd)
#df = pd.read_csv('/Users/David/Dropbox/Python3/git/Datacamp/DataScienceToolbox/tweets.csv')

#counts_dict = pd.read_csv(cwd+'/DataScienceToolbox2/tweets.csv')
chunk=pd.read_csv(cwd+'/DataScienceToolbox2/tweets.csv',chunksize=10)

print(type(chunk))
# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv(cwd+'/DataScienceToolbox2/tweets.csv',chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)
