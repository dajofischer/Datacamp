# Create a figure with the "box_select" tool: p
p = figure(tools='box_select',x_axis_label = 'Year', y_axis_label = 'Time')

# Add circle glyphs to the figure p with the selected and non-selected properties
p.circle('Year','Time',source=source, selection_color = 'red', nonselection_alpha = 0.1 ,nonselection_color = 'blue')

# Specify the name of the output file and show the result
output_file('selection_glyph.html')
show(p)
