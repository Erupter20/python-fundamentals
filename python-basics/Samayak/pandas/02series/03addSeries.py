# 3. Add 5 to each element in the Series [1, 2, 3, 4, 5].

import pandas as pd

data = [1,2,3,4,5]
series = pd.Series(data)
# adding 5 to each element

result = series + 5
print(result) 