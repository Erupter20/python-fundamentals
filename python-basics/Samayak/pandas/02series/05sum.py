# 5. Find the sum of elements in the Series [10, 20, 30, 40].

import pandas as pd
data = [10,20,30,40,50]
series = pd.Series(data)

result = series.sum()
print(result)