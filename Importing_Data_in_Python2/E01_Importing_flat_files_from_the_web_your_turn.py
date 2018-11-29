file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/Importing_Data_in_Python2/'
file = file+'winequality-red.csv'


# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url,filename=file)

# Read file into a DataFrame and print its head
df = pd.read_csv(file, sep=';')
print(df.head())
