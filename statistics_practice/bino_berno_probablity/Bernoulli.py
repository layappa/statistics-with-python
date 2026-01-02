from scipy.stats import bernoulli

# probability of success
p = 0.6

# PMF values
print("P(X=1) =", bernoulli.pmf(1, p))
print("P(X=0) =", bernoulli.pmf(0, p))

# Generate random samples
samples = bernoulli.rvs(p, size=10)
print("Random samples:", samples)
