import numpy as np

data1 = np.array([[1, 2, 3, 4], [11, 22, 44, 33], [10, 30, 40, 20]])
print('Data1 = \n', data1)

data2 = data1[: 4]
data3 = data1[3:]

print('Data2 = \n', data2)
print('Data3 = \n', data3)

