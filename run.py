
from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)

db = client['HamsafarDb']

collection = db.RecSys

from main import getDict

d=getDict()


tt=[]

for key ,val in d.items():
    tt.append((key,val[0][0]))
    


recommandation = db.recommandation

ReclistDb={}
count=0
for i in tt:
    rec={"userId":i[0],
          "placeId":i[1]
          }
    ReclistDb[str(count)]=rec
    count+=1


rec_id = recommandation.insert_one(ReclistDb).inserted_id

    


