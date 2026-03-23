# 3. Accessing Columns by Name
# Using the same DataFrame, access and print the "Age" column.

import pandas as pd

data = {'Name' : ['Alice' , 'Bob', 'Charlie'], 'Age' : [25, 30, 35], 'Department' : ['HR', 'IT', 'Finance']}
df = pd.DataFrame(data)
print(df['Age'])