# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concat([weather_max,weather_mean],axis=1)

# Print weather
print(weather)
