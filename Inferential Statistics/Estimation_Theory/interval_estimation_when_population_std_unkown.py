import numpy as np
from scipy import stats

data = [10, 12, 14, 15, 13]

mean = np.mean(data)
s = np.std(data, ddof=1)   # sample std
n = len(data)

confidence_level = 0.95
alpha = 1 - confidence_level

t = stats.t.ppf(1 - alpha/2, df=n-1)

margin_error = t * (s / np.sqrt(n))
ci = (mean - margin_error, mean + margin_error)

print("CI for Mean (σ unknown):", ci)
