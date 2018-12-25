# Concatenate dataframes: february
february = pd.concat(dataframes,axis=1,keys=['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['Feb.2,2015':'Feb.8,2015', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)
