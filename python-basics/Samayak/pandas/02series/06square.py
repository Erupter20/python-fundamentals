# 6. Apply the square of each element in the Series [2, 4, 6, 8].

import pandas as pd
data = [2,4,6,8]
series = pd.Series(data)
result = series.apply(lambda x: x** 2)
print(result)