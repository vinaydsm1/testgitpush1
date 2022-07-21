import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodb2022:Mongodb2022@cluster0.lq6sr.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "vinay",
    "email": "vinaydsm1@gmail.com",
    "surname": "anand"

}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)