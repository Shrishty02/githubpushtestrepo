import pymongo

client = pymongo.MongoClient("mongodb+srv://Shrishty:Shrishty123@cluster0.i8wwq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
print('hello cutieeee')

d ={
    "name": "shrishty",
    "email" : "shrishty02singh@gmail.com",
    "surname": "singh"
}
db1 = client['mongoddtest']
coll = db1['test']
coll.insert_one(d)