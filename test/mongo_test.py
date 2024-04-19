import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class TestMongoDBConnec(unittest.TestCase):

    def test_mongo_connection(self):
        #Veirifcar la existencia de la bd y su configuracion
        expected_database_name = "postcodes_db"
        expected_collection_name = "postcodes"
        #entorno del test
        mongo_uri = os.getenv("MONGO_URI")
        client = MongoClient(mongo_uri)
        db = client[expected_database_name]
        collection = db[expected_collection_name]

        # verificar nombre de la bd y la collectioin de mongo bd
        self.assertEqual(db.name, expected_database_name)
        self.assertEqual(collection.name, expected_collection_name)

if __name__ == '__main__':
    unittest.main()
