file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/Cleaning_Data_in_Python/'
file = file+'dob_job_application_filings_subset.csv'
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv(file)
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

# Create and display the second scatter plot
df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()
