# Write a Python program to read a JSON file named "student_data.json" into a pandas DataFrame. Print the structure of the DataFrame after loading the JSON file.

import pandas as pd 

# creating a dataframe

data = {'Name':['Alex' , 'Bruce', 'Charlie'], 'Age': [20,22,25]} 
df = pd.DataFrame(data)
# save to json
df.to_json('student data.json', index=False)

# read json
df = pd.read_json('student data.json')

#display the data
print(df)