file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/Cleaning_Data_in_Python/'
file = file+'dob_job_application_filings_subset.csv'
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create the boxplot
df.boxplot(column='initial_cost', by='Borough', rot=90)

# Display the plot
plt.show()
