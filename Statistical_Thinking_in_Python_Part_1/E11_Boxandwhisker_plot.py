# Create box plot with Seaborn's default settings
sns.boxplot(x='species',y='petal length (cm)',data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length')

# Show the plot
plt.show()
