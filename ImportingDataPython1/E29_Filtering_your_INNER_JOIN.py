from sqlalchemy import create_engine
import pandas as pd
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/'
engine = create_engine('sqlite:///'+file+'Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
df = pd.read_sql_query(
    "SELECT * FROM PlaylistTrack INNER JOIN Track ON PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000",
    engine
)

# Print head of DataFrame df
print(df.head())
