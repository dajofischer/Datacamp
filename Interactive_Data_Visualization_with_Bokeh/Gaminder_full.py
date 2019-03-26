import pandas as pd
import matplotlib.pyplot as plt
from bokeh.palettes import brewer
from bokeh.models import HoverTool
from bokeh.models import CategoricalColorMapper
from bokeh.plotting import ColumnDataSource
from bokeh.models import Slider
from bokeh.layouts import widgetbox
from bokeh.io import curdoc


df = pd.read_csv('https://assets.datacamp.com/production/repositories/401/datasets/09378cc53faec573bcb802dce03b01318108a880/gapminder_tidy.csv',
delimiter=',',infer_datetime_format=True,index_col='Year')

print(min(df.index))

source = ColumnDataSource(df.loc[2000])

print(df.loc[1980,'life'].values/10)
print(df.loc[1980,'region'].unique())

regions = df.loc[1980,'region'].unique()


regions_color_dict = dict(zip(regions, brewer['Dark2'][len(regions)]))
print([regions_color_dict[x] for x in df.loc[1980,'region']])
scatter_color = [regions_color_dict[x] for x in df.loc[1980,'region']]

color_mapper = CategoricalColorMapper(factors=regions,
                                      palette=scatter_color)


from bokeh.plotting import figure
from bokeh.io import output_file, show

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle('fertility', 'life',source=source,
color={'field':'region', 'transform':color_mapper},legend='region',
 size = 'life', alpha =0.7)
 #hover_fill_color='firebrick', hover_alpha=0.5,hover_line_color='white')

hover = HoverTool(tooltips = [('Country','@Country')])

# Add the HoverTool object to figure p
p.add_tools(hover)

slider = Slider(title='my slider', start=min(df.index), end=max(df.index), step=1, value=min(df.index))

# Create a widgetbox layout: layout
layout = widgetbox(slider)

# Add the layout to the current document
curdoc().add_root(layout)


# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

# Display the plot
show(p)
