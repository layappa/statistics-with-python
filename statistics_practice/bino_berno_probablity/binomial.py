from scipy.stats import binom

# n = number of trials, p = probability of success
n = 10
p = 0.4

# PMF -> probability of getting k successes
k = 3
print(f"P(X={k}) =", binom.pmf(k, n, p))

# CDF -> probability of <= k successes
print(f"P(X<={k}) =", binom.cdf(k, n, p))

# Generate samples
samples = binom.rvs(n, p, size=10)
print("Random samples:", samples)
