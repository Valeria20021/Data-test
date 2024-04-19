import postcodes
import read_csv
<<<<<<< HEAD
from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import os


load_dotenv()

app = FastAPI()
####################################################################
# Configuración de la conexión a MongoDB
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['postcodes_db']
collection = db['postcodes']



@app.get('/add_postcodes')
def get_list():
    try:
        item, extra_data, outcode = run()

        # Guardar los datos en la base de datos MongoDB
        post_data = {
            'coordenadas': item,
            'postcode': outcode,
            'data': extra_data
        }
        collection.insert_one(post_data)

        # Devolver los datos como respuesta
        return {"message": "Fila añadida a la base de datos correctamente", "data": post_data}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

#############################################


'''
@app.get('/postcodes')
def get_list():
    item, extra_data, outcode = run()
    format = {
        'coordenadas' : item,
        'postcode' : outcode,
        'data' : extra_data
    }
    return format
'''
=======
from mongo_connect import collection
from fastapi import FastAPI, HTTPException
import sys

app = FastAPI()

>>>>>>> develop

def run():
    csv_path_file = './coordenates.csv'
    coordinate_data = read_csv.read_csv(csv_path_file)
    formatted_coordinates = read_csv.format_coordinates_get(coordinate_data)

    requests_sent = 0
<<<<<<< HEAD

    for item in formatted_coordinates:
        try:
            #ejecuta funcion para cada coordenada
            outcode, extra_data= postcodes.get_postcode(item)
            requests_sent += 1
        except ValueError as e:
            print(f'No se encontraron códigos postales para la coordenada: {item}: {e}')

            continue
            # print("extra_data:", extra_data)
            # print("Coordinate:", item)
            # print("Postcode:", outcode)
        if requests_sent >= 4:
            break
    return item, extra_data, outcode



=======
    list_postcodes_insert = []

    for item in formatted_coordinates:
        try:
            #Ejecuta funcion de obtener postcode para cada coordenada
            outcode, extra_data= postcodes.get_postcode(item)
            requests_sent += 1

        except ValueError as e:
            print(f"No se encuentra código postal para las coordenadas: {item}")
            continue
        
        if requests_sent > 7:
            break

# Agregar el documento a la lista de documentos a insertar
        list_postcodes_insert.append({
            'coordenadas': item,
            'postcode': outcode,
            'data': extra_data
        })

    return list_postcodes_insert


@app.get('/add_postcodes')
def send_to_bd_codes():
    try:
        list_to_insert = run()
        if list_to_insert:
            #collection MongoDB
            collection.insert_many(list_to_insert)
            print("Coordenadas añadidas a la base de datos")
        else:
            print("No se encontraron datos para insertar")

        sys.exit()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")
>>>>>>> develop

if __name__ == '__main__':
    run()