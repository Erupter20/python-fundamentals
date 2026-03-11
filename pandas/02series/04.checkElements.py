# 4. Check which elements in the Series [15, 25, 35, 45, 55] are greater than 30.
import pandas as pd
data = [15, 25, 35, 35, 55]
series = pd.Series(data)
result = series > 30
print(result)