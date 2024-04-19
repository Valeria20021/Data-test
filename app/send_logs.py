import time
from mongo_connect import collection

#collecction para registrar logs en MongoDB
logs_collection = collection.logs_db.logs

def log_message(message):
    """Función para insertar un mensaje de registro en la colección de logs."""
    logs_collection.insert_one({"message": message, "timestamp": time.time()})

