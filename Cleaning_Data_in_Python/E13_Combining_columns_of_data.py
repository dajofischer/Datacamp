import pandas as pd
ebola_melt = pd.read_csv('https://assets.datacamp.com/production/course_2023/datasets/ebola.csv')
status_country = pd.read_csv('https://assets.datacamp.com/production/course_2023/datasets/tb.csv')
# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt,status_country],axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())
