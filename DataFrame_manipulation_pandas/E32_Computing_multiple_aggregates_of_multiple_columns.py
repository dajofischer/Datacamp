import pandas as pd
titanic = pd.read_csv('https://assets.datacamp.com/production/repositories/502/datasets/e280ed94bf4539afb57d8b1cbcc14bcf660d3c63/titanic.csv')

# Group titanic by 'pclass': by_class
by_class = titanic.groupby(by='pclass')

# Select 'age' and 'fare'
by_class_sub = by_class[['age','fare']]

# Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max','median'])

# Print the maximum age in each class
print(aggregated.loc[:, ('age','max')])

# Print the median fare in each class
print(aggregated.loc[:, ('fare','median')])
