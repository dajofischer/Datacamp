# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a blue circle glyph to the figure p
p.circle(fertility_latinamerica, female_literacy_latinamerica, size=10, alpha=0.8, color='blue')

# Add a red circle glyph to the figure p

p.circle(fertility_africa, female_literacy_africa, size=10, alpha=0.8, color='red')


# Specify the name of the file
output_file('fert_lit_separate_colors.html')

# Display the plot
show(p)
