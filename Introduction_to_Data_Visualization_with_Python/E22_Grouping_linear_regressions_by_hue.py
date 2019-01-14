# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(x='weight', y='hp', data=auto,hue='origin',palette='Set1')

# Display the plot
plt.show()
