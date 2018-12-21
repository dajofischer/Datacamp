import pandas as pd
medals=pd.read_csv('https://assets.datacamp.com/production/repositories/502/datasets/bf22326ecc9171f68796ad805a7c1135288120b6/all_medalists.csv')

# Group medals by 'NOC': country_grouped
country_grouped = medals.groupby('NOC')


# Compute the number of distinct sports in which each country won medals: Nsports
Nsports = country_grouped['Sport'].nunique()

# Sort the values of Nsports in descending order
Nsports = Nsports.sort_values(ascending=False)

# Print the top 15 rows of Nsports
print(Nsports.head(15))
