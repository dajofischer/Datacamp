import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://assets.datacamp.com/production/course_1761/datasets/percent-bachelors-degrees-women-usa.csv',delimiter=',')
print(df.loc[:,'Year'])

year=df.loc[:,'Year'].values
computer_science=df.loc[:,'Computer Science'].values
physical_sciences=df.loc[:,'Physical Sciences'].values


# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science')
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='lower right')

# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max = computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

# Add a black arrow annotation
plt.annotate('Maximum',xy=(yr_max,cs_max),xytext=(yr_max+5, cs_max+5),arrowprops=dict(facecolor='black'))

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()
