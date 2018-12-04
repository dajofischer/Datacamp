file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/Cleaning_Data_in_Python/'
file = file+'dob_job_application_filings_subset.csv'
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv(file)
wcol=df.columns
print(wcol)
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()
