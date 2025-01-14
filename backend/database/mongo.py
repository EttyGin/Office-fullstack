from pymongo import MongoClient

from database.model import Member

# import model

# from model import Member

class Mongo_connection:
    def __init__(self, connection_str: str, db_name: str, collection_name: str):
        self.client = MongoClient(connection_str)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create(self, member: Member):
        self.collection.insert_one(member.convert())

    def read(self) -> dict:
        return self.collection.find()  # Assuming you want to return all documents as a list of dictionaries

    def delete(self, member_id: str) -> bool:
        result = self.collection.delete_one({"id_num": member_id})
        return result.deleted_count > 0  # Returns True if a document was deleted

    def update(self, member_id: str, updated_data: dict):
        result = self.collection.update_one({"id_num": member_id}, {"$set": updated_data})
        return result.modified_count > 0  # Returns True if a document was modified
    
# Assuming your MongoDB server is running locally and doesn't require authentication
# m = Mongo_connection("mongodb+srv://ettyg325:325746147@cluster0.txtfs.mongodb.net/", "hospital", "members")

# member = Member(
#     id_num="325746147",
#     first_name="John",
#     last_name="Doe",
#     address="Rabbi",
#     phone="0533134012",
#     birth_date=date(1980, 1, 1),
#     illness_start_date=date(2023, 1, 1),
#     illness_end_date=date(2025, 12, 31)
# )
# d = {'id_num': '325746147', 'first_name': 'John', 'last_name': 'Doe', 'address': 'Rabbi'}
# d = {'first_name': 'Try'}
# #m.create(d)
# print("good")
# print(m.update("325746147",d))