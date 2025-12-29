import numpy as np
import pandas as pd

salary=[10000,20000,30000,30000,400000,450000]
age=[22,24,26,28,29,30]

x=np.array(salary)
y=np.array(age)
df=pd.DataFrame( 
    {
      'salary':[10000,20000,30000,30000,400000,450000],
     'age':[22,24,26,28,29,30]

    }
)

def covariance_using_numpy(x,y):
    return np.cov(x,y)

def covariance_using_pandas(df):
    return df.cov()


if __name__=='__main__':
    cov_matrix=covariance_using_numpy(x,y)
    print(cov_matrix)
    print(f"covariance of salary and age is {cov_matrix[0,1]}")
    covariance=covariance_using_pandas(df)

    print(covariance)