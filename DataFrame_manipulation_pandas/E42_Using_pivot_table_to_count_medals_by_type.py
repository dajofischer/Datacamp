import pandas as pd
medals=pd.read_csv('https://assets.datacamp.com/production/repositories/502/datasets/bf22326ecc9171f68796ad805a7c1135288120b6/all_medalists.csv')

# Construct the pivot table: counted
counted = medals.pivot_table(values='Athlete', index='NOC', columns='Medal',aggfunc='count')

# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis=1)

# Sort counted by the 'totals' column
counted = counted.sort_values(by='totals',ascending=False)

# Print the top 15 rows of counted
print(counted.head(15))
