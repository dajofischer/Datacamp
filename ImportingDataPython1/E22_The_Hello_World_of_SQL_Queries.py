# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/'
engine = create_engine('sqlite:///'+file+'Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute('SELECT * from Album')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())
