import pandas as pd
import os

def read_csv(path):
  if not os.path.exists(path):
    raise FileNotFoundError(f'No se encuentra el archivo {path}')

  try:
    csv_data = pd.read_csv(path, sep='|')

    if csv_data.duplicated().any():
            duplicate_rows = csv_data[csv_data.duplicated()].index.tolist()
            raise ValueError(f"El archivo CSV contiene filas duplicadas en las filas: {duplicate_rows}")

    #formato key-value que retorna diccionarios
    data = csv_data.to_dict('records')
    return data
  
  except Exception as error:
     raise RuntimeError(f'No se puede leer el archivo CSV {error}')


def format_coordinates_get(data):
    
     #Formato para GET
     formatted_coordinates = []

     if data['lat'].isnull().any() or data['lon'].isnull().any():
        data_null_coordinates= print("El DataFrame contiene valores faltantes en las columnas 'lat' o 'lon'.")

     for item in data:
         lat = str(item['lat']).replace("'", "").replace(",",".")
         lon = str(item['lon']).replace("'", "").replace(",",".")
         formatted_coordinates.append(f"lon={lon}&lat={lat}")

     return formatted_coordinates
