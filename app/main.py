import controller.postcodes_api as postcodes_api
from model import read_csv
from controller.mongo_connect import collection
from send_logs import log_message
from fastapi import FastAPI, HTTPException
import subprocess


app = FastAPI()

RATE_LIMIT = 2

def run():
    formatted_coordinates = read_csv.format_coordinates_get()

    requests_sent = 0
    list_postcodes_insert = []

    for item in formatted_coordinates:
        try:
            #Ejecuta funcion de obtener postcode para cada coordenada
            outcode, extra_data= postcodes_api.get_postcode(item)
            requests_sent += 1

        except ValueError as e:
            log_message(f"No se encuentra código postal para las coordenadas: {item}")
            continue
        
        if requests_sent > RATE_LIMIT:
            break

        # Agregar los datos a la lista a insertar
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
            result = collection.insert_many(list_to_insert)
            if result.acknowledged:
                print("Coordenadas añadidas a la base de datos")
                return "Coordenadas añadidas a la base de datos"
            else:
                print("Error al añadir coordenadas a la base de datos")
        else:
            print("No se encontraron datos para insertar")

        #termina proceso del servidor
        subprocess.run(["pkill", "-f", "uvicorn"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {e}")

if __name__ == '__main__':
    run()