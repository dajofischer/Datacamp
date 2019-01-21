# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764,715,100000)

# Make the histogram
plt.hist(waiting_times,bins=100,normed=True,histtype='step')


# Label axes
plt.xlabel('Waiting time')
plt.ylabel('count')


# Show the plot
plt.show()
