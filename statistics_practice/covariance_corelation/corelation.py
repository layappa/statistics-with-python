import numpy as np

X = np.array([2, 4, 6, 8, 10])
Y = np.array([5, 9, 12, 18, 25])

corr_matrix = np.corrcoef(X, Y)
print("Correlation Matrix:\n", corr_matrix)

print("Correlation between X & Y:", corr_matrix[0,1])

import pandas as pd

df = pd.DataFrame({
    "X": [2,4,6,8,10],
    "Y": [5,9,12,18,25]
})

print(df.corr())
