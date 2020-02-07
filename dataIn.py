import numpy as np
import pandas as pd

from surprise import Dataset
from surprise import Reader
from pymongo import MongoClient



df3=pd.read_csv('ratings.csv')
df2=df3.sort_values(['placeId'])[:1024]
df2['cityId']="5e344bd08c60197442baf527"

from faker import Faker
faker = Faker()

#fake.name()

namet=[]

ll=df2['userId']

for i in ll:
    namet.append((i,faker.name()))
    

qq=[]
for i in df2.iterrows():
    qq.append(i[1][0])
    

namelist=[]

for i in qq:
    for j in namet:
        if i==j[0]:
            namelist.append(j[1])
            break

df2['name']=namelist
df2['level']=1
df2['score']=0
df2['levelLimit']=15 

print(df2)

#conecting to server



def getDataFrame():
    return df2

















