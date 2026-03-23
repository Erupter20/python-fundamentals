# 2. Accessing Rows by Index
# Using the DataFrame you created in the previous question, access and print the second row.

import pandas as pd

data = {'Name' : ['Alice' , 'Bob', 'Charlie'], 'Age' : [25, 30, 35], 'Department' : ['HR', 'IT', 'Finance']}
df = pd.DataFrame(data)
print(df.loc[1])