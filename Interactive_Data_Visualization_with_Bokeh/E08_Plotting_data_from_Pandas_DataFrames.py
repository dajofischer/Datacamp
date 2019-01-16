# Import pandas as pd
import pandas as pd

# Read in the CSV file: df
df = pd.read_csv('https://assets.datacamp.com/production/repositories/401/datasets/2a776ae9ef4afc3f3f3d396560288229e160b830/auto-mpg.csv')
print(df.head())
# Import figure from bokeh.plotting
from bokeh.plotting import figure
from bokeh.io import output_file,show
# Create the figure: p
p = figure(x_axis_label ='HP', y_axis_label ='MPG')

# Plot mpg vs hp by color
p.circle(df['hp'],df['mpg'],color=df['color'],size=10)

# Specify the name of the output file and show the result
output_file('auto-df.html')
show(p)
