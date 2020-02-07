import pandas as pd
import numpy as np
from dataIn import getDataFrame
from surprise import SVD
from surprise import Dataset
from surprise import Reader
from surprise import accuracy
from surprise.model_selection import cross_validate
from surprise.model_selection import train_test_split


reader = Reader(rating_scale=(1, 5))

data = Dataset.load_from_df(getDataFrame()[['userId', 'placeId', 'rating']],reader)

trainset, testset = train_test_split(data, test_size=.25)

algo=SVD()

algo.fit(trainset)
predictions = algo.test(testset)


print(accuracy.rmse(predictions))

recommendations = []
            
print ("recommend:")
for userID, placeId, actualRating, estimatedRating, _ in predictions:
    intplaceID = int(placeId)
    recommendations.append((userID,intplaceID, estimatedRating))
            
recommendations.sort(key=lambda x: x[0], reverse=True)

reclist=[]
temp=[]
for i in range(0,len(recommendations)-1):
    
    if recommendations[i][0]==recommendations[i+1][0]:
        temp.append(recommendations[i])
    else:
        temp.append(recommendations[i])
        reclist.append(temp)
        temp=[]
        
sRecList=[]
for i in reclist:
    sRecList.append(i[:10])
    
recDict={}
for i in sRecList:
    for j in i:
        if j[0] in recDict.keys():
            recDict[j[0]].append((j[1],))
        else:
            recDict[j[0]]=[(j[1],)]    
            
print(recDict)
            
            
def getDict():           
    return recDict
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    