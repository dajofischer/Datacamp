# Import packages
from sqlalchemy import create_engine
import pandas as pd
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/'
engine = create_engine('sqlite:///'+file+'Chinook.sqlite')

# Create engine: engine
#engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Employee WHERE EmployeeID >=6 ORDER BY BirthDate", engine)

# Print head of DataFrame
print(df.head())
