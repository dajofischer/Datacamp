import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://assets.datacamp.com/production/course_1392/datasets/literacy_birth_rate.csv',delimiter=',',skipfooter=20)
print(df.loc[:,'fertility'])

fertility=df.loc[0:161,'fertility'].values.tolist()
female_literacy=df.loc[0:161,'female literacy'].values.tolist()

print(fertility)

# Import figure from bokeh.plotting
from bokeh.plotting import figure

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(x= fertility, y= female_literacy)

# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

# Display the plot
show(p)
