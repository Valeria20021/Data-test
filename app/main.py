import postcodes
import read_csv

def run():
    csv_path_file = './coordenates.csv'
    #leer archivo y dar formato a coordenadas
    coordinate_data = read_csv.read_csv(csv_path_file)
    formatted_coordinates = read_csv.format_coordinates_get(coordinate_data)
    for item in formatted_coordinates:
        #ejecuta funcion para cada coordenada
        outcode= postcodes.get_postcode(item)
        print("Coordinate:", item)
        print("Postcode:", outcode)
  

if __name__ == '__main__':
    run()
