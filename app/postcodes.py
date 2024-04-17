import requests


def get_postcode(item):
     url= 'https://api.postcodes.io/postcodes?'
     response = requests.get(url,item)

     print(response.status_code)

     data = response.json()
     result = data.get('result', [])
     postcodes_data = []
     #Almacena cada postcode en una lista para cada coordenada
     for codes in result:
            postcode = codes.get('postcode', 'N/A')
            postcodes_data.append(postcode)

     return postcodes_data


