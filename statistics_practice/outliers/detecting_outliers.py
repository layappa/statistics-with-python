import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#DATASET for detecting outlires
data = {
    'Salary': [25, 28, 30, 32, 35, 36, 38, 40, 42, 100, 120],
    'Age':    [22, 23, 24, 25, 26, 70, 27, 28, 29, 30, 90]
}

df = pd.DataFrame(data)
print("Original Data\n", df)

#function to detect outlires
#visualization
def plot_outlires(series):
    fig, axes = plt.subplots(1, 2, figsize=(10,4))
    sns.boxplot(x=series,ax=axes[0])
    plt.title(f"outlires for {series}")

    sns.histplot(x=series,kde=True,ax=axes[1])
    plt.show()


#finding outlires using iqr method
def find_outlires_iqr(coulmn):
    q1=coulmn.quantile(0.25)
    q3=coulmn.quantile(0.75)

    IQR=q3-q1
    lower=q1-1.5*IQR
    upper=q3+1.5*IQR
    outlires=coulmn[(coulmn<lower)|(coulmn>upper)]
    return outlires,lower,upper

if __name__=='__main__':
    plot_outlires(df['Salary'])
    #plot_outlires(df['Age'])
    outliers,lower,upper=find_outlires_iqr(df['Salary'])

    print("Outliers:\n", outliers)
    print("Lower bound:", lower)
    print("Upper bound:", upper)

    