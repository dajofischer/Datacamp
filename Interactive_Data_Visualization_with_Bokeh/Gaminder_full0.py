import pandas as pd
import matplotlib.pyplot as plt
from bokeh.palettes import brewer
from bokeh.models import HoverTool
from bokeh.models import CategoricalColorMapper
from bokeh.plotting import ColumnDataSource
from bokeh.models import Slider
from bokeh.layouts import widgetbox, row
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.io import output_file, show

df = pd.read_csv('https://assets.datacamp.com/production/repositories/401/datasets/09378cc53faec573bcb802dce03b01318108a880/gapminder_tidy.csv',
delimiter=',',infer_datetime_format=True,index_col='Year')
source = ColumnDataSource(df)

print(df.head())

regions = df.loc[1980,'region'].unique()


regions_color_dict = dict(zip(regions, brewer['Dark2'][len(regions)]))
print([regions_color_dict[x] for x in df.loc[1980,'region']])
scatter_color = [regions_color_dict[x] for x in df.loc[1980,'region']]

color_mapper = CategoricalColorMapper(factors=regions,
                                      palette=scatter_color)

plot = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')
plot.circle(x='life', y='fertility', fill_alpha=0.8, source=source,
            color=dict(field='region', transform=color_mapper), legend='region')

# Set the legend.location attribute of the plot to 'top_right'
plot.legend.location = 'top_right'
# Define the callback: update_plot
def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value
    x = x_select.value
    y = y_select.value
    # Label axes of plot
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y
    # Set new_data
    new_data = {
        'x'       : df.loc[yr][x],
        'y'       : df.loc[yr][y],
        'country' : df.loc[yr].Country,
        'pop'     : (df.loc[yr].population / 20000000) + 2,
        'region'  : df.loc[yr].region,
    }
    # Assign new_data to source.data
    source.data = new_data

    # Set the range of all axes
    plot.x_range.start = min(df[x])
    plot.x_range.end = max(df[x])
    plot.y_range.start = min(df[y])
    plot.y_range.end = max(df[y])

    # Add title to plot
    plot.title.text = 'Gapminder data for %d' % yr





# Create a dropdown slider widget: slider
slider = Slider(title='Select Year', start=min(df.index), end=max(df.index), step=1, value=min(df.index))
# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Create a dropdown Select widget for the x data: x_select
x_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='fertility',
    title='x-axis data'
)

# Attach the update_plot callback to the 'value' property of x_select
x_select.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select
y_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='life',
    title='y-axis data'
)

# Attach the update_plot callback to the 'value' property of y_select
y_select.on_change('value',update_plot)

# Create layout and add to current document
layout = row(widgetbox(slider, x_select, y_select), plot)
curdoc().add_root(layout)
