from typing import Dict, List
from bson.objectid import ObjectId

class MapInfoRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "map_info"
        self.__db_connection = db_connection
#Inserir
    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    def insert_list_of_documents(self, list_of_documents: List[Dict]):
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents
    
#Busca
    def select_many(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filter, {"_id": 0}) # Remove parametro
        response = []
        for elem in data: response.append(elem)
        return response
    
    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({"name": filter}, {"id": 0})
        return response
    
    def select_if_property_existis(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find( {filter: {"$exists": True}}, {"id" :0})
        response = []
        for elem in data: response.append(elem)
        return response
    
    def select_many_order(self, filter, filter2) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filter, {"_id": 0}).sort([(filter2)]) # filter2 exem: ()"pedidos.pizza", 1)
        response = []
        for elem in data: response.append(elem)
        return response
    
    def select_or(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "$or": [filter] })
        response = []
        for elem in data: response.append(elem)
        return response
    
    def select_by_object_id(self, id) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "_id": ObjectId(id) })
        response = []
        for elem in data: response.append(elem)
        return response