# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = '/Volumes/Data/Dropbox/Python3/git/Datacamp/ImportingDataPython1/'
file = file+'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
