from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.plsmp.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.update_one({'title':'장민호 드라마 최종회'},{'$set':{'star':'8.78'}})