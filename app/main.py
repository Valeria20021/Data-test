import postcodes
import read_csv
from mongo_connect import collection
from fastapi import FastAPI, HTTPException
import sys

app = FastAPI()


def run():
    csv_path_file = './coordenates.csv'
    coordinate_data = read_csv.read_csv(csv_path_file)
    formatted_coordinates = read_csv.format_coordinates_get(coordinate_data)

    requests_sent = 0
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

if __name__ == '__main__':
    run()
