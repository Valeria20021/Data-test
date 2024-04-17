import csv

def read_csv(path):
  
  #Cierre de archivo automaticamente al terminar ejecucion
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='|')
    header = next(reader)
    data = []
    #recorre archivo CSV
    for row in reader:
      iterable = zip(header, row)
      #Formato de diccionario
      coordinates = {key: value for key, value in iterable}
      data.append(coordinates)
    return data


def format_coordinates_get(data):
    #Formato para GET
    formatted_coordinates = []
    for item in data:
        lat = item['lat'].replace("'", "")
        lon = item['lon'].replace("'", "")
        formatted_coordinates.append(f"lat={lat}&lon={lon}")
    return formatted_coordinates


if __name__ == '__main__':
    
    #Definicion de archivo
    csv_path_file = './coordenates.csv'
    coordinate_data = read_csv(csv_path_file)
    formatted_coordinates = format_coordinates_get(coordinate_data)
    for item in formatted_coordinates:
        print(item)



