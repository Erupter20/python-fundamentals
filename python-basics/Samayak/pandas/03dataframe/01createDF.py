#Create a DataFrame from a dictionary that contains the following data:
# •Name: ["Alice", "Bob", "Charlie"]
# •Age: [25, 30, 35]
# •Department: ["HR", "IT", "Finance"]
# After creating the DataFrame, print it.

import pandas as pd

data = {'Name' : ['Alice' , 'Bob', 'Charlie'], 'Age' : [25, 30, 35], 'Department' : ['HR', 'IT', 'Finance']}

res = pd.DataFrame(data)
print(res)
