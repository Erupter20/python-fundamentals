# 1. Handling Missing Data (NaN)
# Create a DataFrame with the following data:
# •Name: ["Alice", "Bob", "Charlie"]
# •Age: [25, None, 35]
# •Department: ["HR", "IT", None]
# Handle the missing values by:
# •Replacing all missing values with "Unknown" for the string columns.
# •Replacing the missing values in the "Age" column with the average age of the non-missing values.

import pandas as pd

# creating a dataframe

data = {'Name' :['Alex', 'Bob', 'Charlie'], 'Age' : [25, None, 35], 'Department': ["HR", "IT", None]}

df = pd.DataFrame(data)

# replacing missing age with its average
average_age = df[['Age']].mean()

# Handle missing values
df_filled = df.fillna({'Age' : average_age, 'Department': "Unknown"})

print(df_filled)