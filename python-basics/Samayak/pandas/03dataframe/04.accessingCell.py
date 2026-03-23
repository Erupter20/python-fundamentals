# 4. Accessing Specific Cell by Row and Column
# Access and print the age of the second person in the DataFrame (using the row index and column name).

import pandas as pd

data = {'Name' : ['Alice' , 'Bob', 'Charlie'], 'Age' : [25, 30, 35], 'Department' : ['HR', 'IT', 'Finance']}
df = pd.DataFrame(data)
print(df.loc[1, 'Age'])
