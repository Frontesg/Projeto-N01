from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/?directConnection=true"
client = MongoClient(connection_string)
db_connection = client["Projeto-N01"]
collection = db_connection.get_collection("pj01")

search_filter = {"nome":"Ouyos-Aoeuam"}
response = collection.find(search_filter)

for registry in response: print(registry)
""" collection.insert_one({
    "test":"numero1",
    "Numeros":[123,456,789]
}) """

