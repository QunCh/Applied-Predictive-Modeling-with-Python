import pyreadr
result = pyreadr.read_r('D:\LEARNING\Applied-Predictive-Modeling-with-Python\data\cars.Rdata')
r = pyreadr.read_r('BloodBrain.RData')
type(result)

print(result.keys())
data = result['cars']
type(result['cars'])
data.head()

import os
os.chdir('D:\LEARNING\Applied-Predictive-Modeling-with-Python\data')
for file in os.listdir():
    print(file)
    result = pyreadr.read_r(file)
    print(result.keys())

