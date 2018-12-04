file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/Cleaning_Data_in_Python/'
file = file+'dob_job_application_filings_subset.csv'
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

print(df.info())

print(df['City'])

# Print the head and tail of df_subset
#print(df_subset.head())
#print(df_subset.tail())
