import csv

def read_csv(path):
  
  #With para cerrar archivo automaticamente al terminar ejecucion
  with open(path, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter='|')
    #Primera linea iterada definida como header
    header = next(reader)
    data = []
    
    #recorrer archivo CSV
    for row in reader:
      
      iterable = zip(header, row)
      #dar formato de diccionario
      coordenates = {key: value for key, value in iterable}
     
      data.append(coordenates)
    return data


if __name__ == '__main__':
  # Envio de parametro path a la funcion read_csv
  data = read_csv('./coordenates.csv')
  print(data)


