import pandas as pd
import matplotlib.pyplot as plt
from bokeh.palettes import brewer
from bokeh.models import HoverTool, Label
from bokeh.models import CategoricalColorMapper
from bokeh.plotting import ColumnDataSource
from bokeh.models import Slider
from bokeh.layouts import widgetbox, column
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from bokeh.io import output_file, show
import numpy as np
from scipy.stats import gaussian_kde
from bokeh.util.hex import hexbin

size_background = 100
size_peak = 10
length_data = 1000

datax=np.random.random([size_background,length_data])-0.5
datay=np.random.random([size_background,length_data])-0.5

peakx=(np.random.random([size_peak,length_data])-0.5)/5
peaky=(np.random.random([size_peak,length_data])-0.5)/5

datax = np.concatenate((datax,peakx),axis=0)
datay = np.concatenate((datay,peaky),axis=0)

size_background = size_background + size_peak


bins = hexbin(datax[:,0], datay[:,0], 0.01)

#print(np.reshape(datax[0:5,0:2],(10,1))[:,0])
#print(datax[0:10,0])

source = ColumnDataSource(data={
    'x'       : datax[:,0],
    'y'       : datay[:,0],
})

# Save the minimum and maximum values of the fertility column: xmin, xmax
#xmin, xmax = min(data.fertility), max(data.fertility)

# Save the minimum and maximum values of the life expectancy column: ymin, ymax
#ymin, ymax = min(data.life), max(data.life)

# Create the figure: plot
plot = figure(title='Gapminder Data for 1970', plot_height=700, plot_width=700)

# Add circle glyphs to the plot
#plot.circle(x='x', y='y', fill_alpha=0.8, source=source)
plot.hex_tile(q="q", r="r",source = bins,  size=0.01)


#countrylabel = Label(x=data.loc[1970].fertility[data.loc[1970].Country == 'China'],
#y = data.loc[1970].life[data.loc[1970].Country == 'China'],  text = 'China')

def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value

    # Set new_data
    new_data = {
        'x'       : np.reshape(datax[:,0:yr],(size_background*yr,1))[:,0],
        'y'       : np.reshape(datay[:,0:yr],(size_background*yr,1))[:,0]
    }
    # Assign new_data to source.data

    newdata = hexbin(np.reshape(datax[:,0:yr],(size_background*yr,1))[:,0],
    np.reshape(datay[:,0:yr],(size_background*yr,1))[:,0], 0.01)

    bins.data = newdata
    # Set the range of all axes


# Create a dropdown slider widget: slider
slider = Slider(start=1, end=length_data, step=1, value=1, title='# samples')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Add the HoverTool object to figure p
#plot.add_tools(hover)
#plot.add_layout(countrylabel)
# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)
