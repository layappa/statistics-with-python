from sklearn.preprocessing import MinMaxScaler
import numpy as np
data=[10,20,30,10,23,45]


def normalization_manually(min,max,data):
    normalized=[(x-min)/(max-min) for x in data]
    return normalized
def normalized_using_standrd_scalar():
    scalar=MinMaxScaler()
    data = np.array([[10,20,30,10,23,45]])
    data=data.reshape(-1,1)
    return scalar.fit_transform(data)

if __name__=="__main__":
    normalized=normalization_manually(min(data),max(data),data)
    normalized_1=normalized_using_standrd_scalar()

    print(f"normalized data : {normalized}")
    print(f"normalized data using minmaxscalar : {normalized_1}")
