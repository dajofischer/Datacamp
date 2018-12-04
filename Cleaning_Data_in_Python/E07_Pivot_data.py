# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=['Month','Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())
