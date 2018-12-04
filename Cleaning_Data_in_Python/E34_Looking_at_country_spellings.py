# Create the series of countries: countries
countries = ____

# Drop all the duplicates from countries
countries = ____

# Write the regular expression: pattern
pattern = '^[____]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(____)

# Invert the mask: mask_inverse
mask_inverse = ____

# Subset countries using mask_inverse: invalid_countries
invalid_countries = ____

# Print invalid_countries
print(invalid_countries)
