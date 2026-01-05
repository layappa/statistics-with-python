import numpy as np
from scipy import stats

# -----------------------------
# Point Estimate (Sample Mean)
# -----------------------------
def point_estimate(data):
    return np.mean(data)


# -----------------------------
# Margin of Error (Z or t auto)
# -----------------------------
def margin_of_error(data, confidence=0.95, sigma=None):
    data = np.array(data)
    n = len(data)
    se = (sigma / np.sqrt(n)) if sigma else np.std(data, ddof=1) / np.sqrt(n)

    # Z-critical (sigma known)
    if sigma:
        crit = stats.norm.ppf((1 + confidence) / 2)
    # t-critical (sigma unknown)
    else:
        crit = stats.t.ppf((1 + confidence) / 2, df=n-1)

    return crit * se


# -----------------------------
# Confidence Interval
# -----------------------------
def confidence_interval(data, confidence=0.95, sigma=None):
    mean = point_estimate(data)
    moe = margin_of_error(data, confidence, sigma)
    return mean, mean - moe, mean + moe


# =============================
# Example — Sample Data
# =============================
sample = [158, 160, 162, 155, 165, 159, 161, 163]

mean, L, U = confidence_interval(sample, confidence=0.95)

print("Point Estimate (Sample Mean):", round(mean, 2))
print("Margin of Error:", round(mean - L, 2))
print("95% Confidence Interval:", round(L, 2), "to", round(U, 2))
