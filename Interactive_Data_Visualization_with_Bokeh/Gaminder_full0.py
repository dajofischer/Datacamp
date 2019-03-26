import pandas as pd
import matplotlib.pyplot as plt
from bokeh.palettes import brewer
from bokeh.models import HoverTool, Label
from bokeh.models import CategoricalColorMapper
from bokeh.plotting import ColumnDataSource
from bokeh.models import Slider
from bokeh.layouts import widgetbox, row
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.io import output_file, show

data = pd.read_csv('https://assets.datacamp.com/production/repositories/401/datasets/09378cc53faec573bcb802dce03b01318108a880/gapminder_tidy.csv',
delimiter=',',infer_datetime_format=True,index_col='Year')



regions_list = data.region.unique().tolist()
country_list = data.Country.unique().tolist()


colormap = brewer['Dark2'][len(regions_list)]

color_mapper = CategoricalColorMapper(factors=regions_list,
                                      palette=colormap)


source = ColumnDataSource(data={
    'x'       : data.loc[1970].fertility,
    'y'       : data.loc[1970].life,
    'country'      : data.loc[1970].Country,
    'pop'      : (data.loc[1970].population / 20000000) + 2,
    'region'      : data.loc[1970].region
})

# Save the minimum and maximum values of the fertility column: xmin, xmax
xmin, xmax = min(data.fertility), max(data.fertility)

# Save the minimum and maximum values of the life expectancy column: ymin, ymax
ymin, ymax = min(data.life), max(data.life)

# Create the figure: plot
plot = figure(title='Gapminder Data for 1970', plot_height=400, plot_width=700,
              x_range=(xmin, xmax), y_range=(ymin, ymax))

# Add circle glyphs to the plot
plot.circle(x='x', y='y', fill_alpha=0.8, source=source,
color=dict(field='region', transform=color_mapper), legend='region', size = 'pop')
plot.legend.location = 'top_right'

#countrylabel = Label(x=data.loc[1970].fertility[data.loc[1970].Country == 'China'],
#y = data.loc[1970].life[data.loc[1970].Country == 'China'],  text = 'China')
countrylabel = Label(x=data.loc[1970].fertility[data.loc[1970].Country == 'China'].values[0],
y = data.loc[1970].life[data.loc[1970].Country == 'China'].values[0],  text = 'China')

def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value
    x = x_select.value
    y = y_select.value
    ctr = z_select.value
    # Label axes of plot
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y
    # Set new_data
    new_data = {
        'x'       : data.loc[yr][x],
        'y'       : data.loc[yr][y],
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    # Assign new_data to source.data
    source.data = new_data

    # Set the range of all axes
    plot.x_range.start = min(data[x])
    plot.x_range.end = max(data[x])
    plot.y_range.start = min(data[y])
    plot.y_range.end = max(data[y])

    # Add title to plot
    plot.title.text = 'Gapminder data for %d' % yr

    countrylabel.x = data.loc[yr].fertility[data.loc[yr].Country == ctr].values[0]
    countrylabel.y = data.loc[yr].life[data.loc[yr].Country == ctr].values[0]
    countrylabel.text = ctr

# Create a dropdown slider widget: slider
slider = Slider(start=min(data.index), end=max(data.index), step=1, value=1970, title='Year')

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

z_select = Select(
    options=country_list,
    value='China',
    title='Track Country'
)

z_select.on_change('value',update_plot)

hover = HoverTool(tooltips = [('Country','@country')])

# Add the HoverTool object to figure p
plot.add_tools(hover)
plot.add_layout(countrylabel)
# Create layout and add to current document
layout = row(widgetbox(slider, x_select, y_select, z_select), plot)
curdoc().add_root(layout)
