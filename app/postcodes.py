import requests

def get_postcode(item):
     url= 'https://api.postcodes.io/postcodes?'
     response = requests.get(url,item)
     data = response.json()
     result = data.get('result', [])

     if result is None:
            print("No se encontraron códigos postales para la coordenada:", item)
            return ['null']
     #Almacena cada codigo en la lista
     postcodes = [codes.get('postcode', 'N/A') for codes in result]

     return postcodes,data

