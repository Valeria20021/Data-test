import pandas as pd
import numpy as np
import os


def read_csv(path):
  if not os.path.exists(path):
    raise FileNotFoundError(f'No se encuentra el archivo {path}')
  
  if not path.endswith('.csv'):
    raise ValueError(f'El archivo {path} no es un archivo CSV')

  csv_data = pd.read_csv(path, sep='|')

  #Eliminar datos duplicados o sin valor
  csv_data.drop_duplicates(inplace=True)
  csv_data.dropna(subset=['lat', 'lon'], inplace=True)

  if csv_data.duplicated().any():
     csv_data[csv_data.duplicated()].index.tolist()
     raise ValueError(f"El archivo CSV contiene filas duplicadas")
  
  if csv_data['lat'].isnull().any() or csv_data['lon'].isnull().any():
     raise ValueError("El archivo CSV contiene valores NaN en las columnas 'lat' o 'lon'.")


    #formato key-value que retorna diccionarios
  data = csv_data.to_dict('records')
  return data


def format_coordinates_get(data):
    
     #Formato para GET
     formatted_coordinates = []
     
     for item in data:
         lat = str(item['lat']).replace("'", "").replace(",",".")
         lon = str(item['lon']).replace("'", "").replace(",",".")

         # Verificar si las coordenadas no son 'nan' antes de agregarlas
         if lat != 'nan' and lon != 'nan':
          formatted_coordinates.append(f"lon={lon}&lat={lat}")


     return formatted_coordinates
