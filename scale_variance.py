# -*- coding:utf-8 -*-

import numpy as np
from sklearn import preprocessing

np_array = np.array([[1,2,3],[4,5,6]])
np.max(np_array[:,1])
np.min(np_array[:,1])
np.mean(np_array[:,1])

# first,normalization | seconed,get variance
# x-min/max-min
def var(lists,k):
    singe_data = np.reshape(lists[:,k],(-1,1))
    scaler = preprocessing.MinMaxScaler()
    scaler.data_max_
    scale_data = scaler.transform(singe_data)
    return np.var(scale_data)
