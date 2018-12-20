# Unstack users by 'city': bycity
bycity = users.unstack(0)

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack(level='city'))
