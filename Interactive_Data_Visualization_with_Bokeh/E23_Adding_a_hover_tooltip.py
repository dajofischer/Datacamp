import pandas as pd
import matplotlib.pyplot as plt
from bokeh.models import ColumnDataSource

df = pd.read_csv('https://assets.datacamp.com/production/course_1392/datasets/literacy_birth_rate.csv',delimiter=',',skipfooter=20)
print(df.loc[:,'Continent'])

print(df.loc[:,'fertility'])

fertility=df.loc[0:161,'fertility'].values.tolist()
female_literacy=df.loc[0:161,'female literacy'].values.tolist()

latin_america = df.loc[df.loc[:,'Continent']=='LAT',:]
latin_america.columns=['Country', 'Continent', 'female literacy', 'fertility', 'population']
print(latin_america.columns)
latin_america =ColumnDataSource(latin_america)

africa = df.loc[df.loc[:,'Continent']=='AF',:]
africa.columns=['Country', 'Continent', 'female literacy', 'fertility', 'population']
print(africa.columns)
africa =ColumnDataSource(africa)

print(africa)

from bokeh.plotting import figure
from bokeh.io import output_file,show
p = figure(x_axis_label = 'fertility', y_axis_label = 'female literacy')
# Add the first circle glyph to the figure p
p.circle('fertility', 'female literacy', source=latin_america, size=10, color='red', legend='Latin America')

# Add the second circle glyph to the figure p
p.circle('fertility', 'female literacy', source=africa, size=10, color='blue', legend='Africa')


# Assign the legend to the bottom left: p.legend.location
p.legend.location='bottom_left'

# Fill the legend background with the color 'lightgray': p.legend.background_fill_color
p.legend.background_fill_color='lightgray'

# Specify the name of the output_file and show the result



# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool object: hover
hover = HoverTool(tooltips = [('Country','@Country')])

# Add the HoverTool object to figure p
p.add_tools(hover)

# Specify the name of the output_file and show the result
output_file('hover.html')
show(p)
