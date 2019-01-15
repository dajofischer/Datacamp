# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle(x=fertility_latinamerica ,y=female_literacy_latinamerica)

# Add an x glyph to the figure p
p.x(x=fertility_africa ,y=female_literacy_africa)

# Specify the name of the file
output_file('fert_lit_separate.html')

# Display the plot
show(p)
