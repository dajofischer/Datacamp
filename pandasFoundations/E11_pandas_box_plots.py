# Make a list of the column names to be plotted: cols
cols = ['weight','mpg']

# Generate the box plots
df[cols].plot(subplots=True,kind='box')

# Display the plot
plt.show()
