import pandas as pd
titanic = pd.read_csv('https://assets.datacamp.com/production/repositories/502/datasets/e280ed94bf4539afb57d8b1cbcc14bcf660d3c63/titanic.csv')

print(titanic.describe())

# Group titanic by 'pclass'
by_class = titanic.groupby(by='pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()

# Print count_by_class
print(count_by_class)

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(by=['embarked' , 'pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['survived'].count()

# Print count_mult
print(count_mult)
