import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('https://assets.datacamp.com/production/repositories/497/datasets/4e8cdfbf9e125bb723981f9218bee16194c7d869/messy_stock_data.tsv', delimiter=' ', header=None, comment='#',skiprows=3)
df.to_csv('messy_stock_data.csv')
df=df.transpose()

index=df.iloc[0,:]
index[0]='Month'

df.columns=index
df=df.iloc[1:,:]
print(df.head())
for x in range(1,5):
    df.iloc[:,x]=pd.to_numeric(df.iloc[:,x])

print(df.head())
print(df.dtypes)
# Create a list of y-axis column names: y_columns
y_columns = ['APPLE','IBM']

# Generate a line plot
df.plot(x='Month', y=y_columns)

# Add the title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# Display the plot
plt.show()

print(df.describe())
