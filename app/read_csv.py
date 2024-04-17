import pandas as pd

def read_csv(path):
  
    csv_data = pd.read_csv(path, sep='|')
    #formato key-value que retorna diccionarios
    data = csv_data.to_dict('records')
    return data


def format_coordinates_get(data):
     #Formato para GET
     formatted_coordinates = []
     for item in data:
         lat = str(item['lat']).replace("'", "").replace(",",".")
         lon = str(item['lon']).replace("'", "").replace(",",".")
         formatted_coordinates.append(f"lon={lon}&lat={lat}")
     return formatted_coordinates
