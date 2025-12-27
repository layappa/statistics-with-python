import pandas as pd
from detecting_outliers import find_outlires_iqr
data = {
    'Salary': [25, 28, 30, 32, 35, 36, 38, 40, 42, 100, 120],
    'Age':    [22, 23, 24, 25, 26, 70, 27, 28, 29, 30, 90]
}

df = pd.DataFrame(data)
print("Original Data\n", df)
#functions to remove outlires

def remove_outliers_iqr(series):
    outliers, lower, upper =find_outlires_iqr(series)
    return series[(series >= lower) & (series <= upper)]

df["Salary_Removed"] = remove_outliers_iqr(df["Salary"])
print("\nSalary After Removing Outliers\n", df["Salary_Removed"])