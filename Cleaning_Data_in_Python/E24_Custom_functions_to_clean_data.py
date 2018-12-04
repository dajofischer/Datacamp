# Define recode_gender()
def recode_gender(gender):

    # Return 0 if gender is 'Female'
    if gender == 'Female':
        return 0

    # Return 1 if gender is 'Male'
    elif gender == 'Male':
        return 1

    # Return np.nan
    else:
        return np.nan

# Apply the function to the sex column
tips['recode'] = tips['sex'].apply(recode_gender)

# Print the first five rows of tips
print(tips.head())
