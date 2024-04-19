from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()

# Configuración de la conexión a MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['postcodes_db']
collection = db['postcodes']