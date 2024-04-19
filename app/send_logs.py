import time
from controller.mongo_connect import collection

#collecction para registrar logs en MongoDB
logs_collection = collection.logs_db.logs

def log_message(message):
    logs_collection.insert_one({"message": message, "timestamp": time.time()})

