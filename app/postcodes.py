import requests


def get_postcode(item):
     url= 'https://api.postcodes.io/postcodes?'
     r = requests.get(url,item)

     print(r.status_code)

     data = r.json()
     result = data.get('result', [])
     postcodes_data = []
     #Almacena cada postcode en una lista para cada coordenada
     for codes in result:
            postcode = codes.get('postcode', 'N/A')
            postcodes_data.append(postcode)

     return postcodes_data


