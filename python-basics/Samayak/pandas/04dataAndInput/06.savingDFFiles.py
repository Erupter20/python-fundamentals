# Using the DataFrame from question #1, save the DataFrame as a JSON file named "employees.json" and then load it again into a new DataFrame. Print the loaded DataFrame.

import pandas as pd

# read csv
df = pd.read_csv('employees_output.csv')

# save as json
 
df.to_json("employees_output.json", index = False)

print(df)
