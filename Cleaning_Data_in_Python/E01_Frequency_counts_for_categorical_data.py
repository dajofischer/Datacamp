file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/Cleaning_Data_in_Python/'
file = file+'dob_job_application_filings_subset.csv'
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))
