# Create ColumnDataSource: source
source = ColumnDataSource(data)

# Create the first figure: p1
p1 = figure(x_axis_label='fertility (children per woman)', y_axis_label='female literacy (% population)',
            tools='box_select,lasso_select')

# Add a circle glyph to p1
p1.circle('fertility','female literacy',source=source)

# Create the second figure: p2
p2 = figure(x_axis_label='fertility (children per woman)', y_axis_label='population (millions)',tools='box_select,lasso_select')

# Add a circle glyph to p2
p2.circle('fertility','population',source=source)

# Create row layout of figures p1 and p2: layout
layout = row([p1,p2])

# Specify the name of the output_file and show the result
output_file('linked_brush.html')
show(layout)
