import pandas as pd
gapminder = pd.read_csv('https://assets.datacamp.com/production/repositories/502/datasets/09378cc53faec573bcb802dce03b01318108a880/gapminder_tidy.csv',index_col=['Year','region','Country']).sort_index()


# Group gapminder by 'Year' and 'region': by_year_region
by_year_region = gapminder.groupby(level=['Year' , 'region'])

# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()

# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Print the last 6 entries of aggregated
print(aggregated.tail(6))
