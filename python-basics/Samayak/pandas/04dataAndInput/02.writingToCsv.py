# 2. Writing to a CSV File
# Using a DataFrame you create with the following data:
# •Name: ["Alice", "Bob", "Charlie"]
# •Age: [25, 30, 35]
# •Department: ["HR", "IT", "Finance"]
# Write this DataFrame to a CSV file named "employees_output.csv". Ensure the index is not saved in the file.

import pandas as pd
data = {'Name' :['Alex', 'Bob', 'Charlie'], 'Age' : [20, 21, 22]}
df = pd.DataFrame(data)
df.to_csv('employees_output.csv', index=False)
df = pd.read_csv('employess_output.csv')
print(df)
