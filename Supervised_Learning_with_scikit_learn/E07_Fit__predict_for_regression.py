# Import LinearRegression
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame: df
df = pd.read_csv('https://assets.datacamp.com/production/course_6078/datasets/gm_2008_region.csv')

# Create arrays for features and target variable
y = df['life'].values

X=df.drop( columns=['life','Region'],axis=1).values
X_fertility = df['fertility'].values

y = y.reshape(-1,1)
X_fertility = X_fertility.reshape(-1,1)

print(df.info())

# Create the regressor: reg
reg = LinearRegression()

# Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1,1)

# Fit the model to the data
reg.fit(X,y)

# Compute predictions over the prediction space: y_pred
#y_pred = reg.predict(prediction_space)

# Print R^2
print(reg.score(X,y))

# Plot regression line
plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.show()
