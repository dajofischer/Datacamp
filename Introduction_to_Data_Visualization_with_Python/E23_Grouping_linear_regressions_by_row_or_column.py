# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight', y='hp', data=auto,row='origin',palette='Set1')


# Display the plot
plt.show()
