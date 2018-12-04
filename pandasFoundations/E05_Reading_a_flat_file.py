import pandas as pd
# Read in the file: df1
df1 = pd.read_csv('https://assets.datacamp.com/production/repositories/497/datasets/cc1de7b583ec7eb6196df30845d32241fe15d643/world_population.csv')

# Create a list of the new column labels: new_labels
new_labels = ['year', 'population']

# Read in the file, specifying the header and names parameters: df2
df2 = pd.read_csv('https://assets.datacamp.com/production/repositories/497/datasets/cc1de7b583ec7eb6196df30845d32241fe15d643/world_population.csv', header=0, names=new_labels)

# Print both the DataFrames
print(df1)
print(df2)
