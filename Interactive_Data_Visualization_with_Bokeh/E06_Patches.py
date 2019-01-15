# Create a list of az_lons, co_lons, nm_lons and ut_lons: x
x = [az_lons, co_lons, nm_lons, ut_lons]

# Create a list of az_lats, co_lats, nm_lats and ut_lats: y
y = [az_lats, co_lats, nm_lats,  ut_lats]

# Add patches to figure p with line_color=white for x and y
p.patches(x,y,line_color='white')

# Specify the name of the output file and show the result
output_file('four_corners.html')
show(p)
