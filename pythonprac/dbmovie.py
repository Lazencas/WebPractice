from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:test@cluster0.79zcl6d.mongodb.net/test')
db = client.dbpracticeman


movies = db.movies.find_one({'title':'가버나움'})['point']
point = movies

all_movies = list(db.movies.find({'point':point},{'_id':False}))
for m in all_movies:
    print(m['title'])

db.movies.update_one({'title':'가버나움'},{'$set':{'point':'0'}})