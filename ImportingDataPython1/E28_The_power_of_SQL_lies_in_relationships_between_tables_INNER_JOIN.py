from sqlalchemy import create_engine
import pandas as pd
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/'
engine = create_engine('sqlite:///'+file+'Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
     rs = con.execute("SELECT Title,Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())
