import pyreadr
result = pyreadr.read_r(r'C:\Users\qunch\Documents\GitHub\AppliedPredictiveModeling_1.1-7\AppliedPredictiveModeling\data\segmentationOriginal.Rdata')
result.keys()
data = result['segmentationOriginal']
data.head()
data.to_csv("segmentationOriginal.csv", index = False)