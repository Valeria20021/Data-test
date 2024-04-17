import pandas as pd

def read_csv(path):
  
    data_csv = pd.read_csv(path, sep='|')
    #formato key-value que retorna diccionarios es records en pandas
    data = data_csv.to_dict('records')

    return data


def format_coordinates_get(data):
     #Formato para GET
     formatted_coordinates = []
     for item in data:
         lat = str(item['lat']).replace("'", "").replace(",",".")
         lon = str(item['lon']).replace("'", "").replace(",",".")
         formatted_coordinates.append(f"lon={lon}&lat={lat}")
     return formatted_coordinates
