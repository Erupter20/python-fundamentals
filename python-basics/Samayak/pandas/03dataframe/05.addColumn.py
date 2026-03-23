# 5. Adding a New Column
# Add a new column named "Salary" to the DataFrame with values: [50000, 60000, 70000]. Print the updated DataFrame.


import pandas as pd

data = {'Name' : ['Alice' , 'Bob', 'Charlie'], 'Age' : [25, 30, 35], 'Department' : ['HR', 'IT', 'Finance']}
df = pd.DataFrame(data)
df['Salary'] = [50000,60000,55000]
print(df.loc[1])