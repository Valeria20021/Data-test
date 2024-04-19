import requests

def get_postcode(item):
     url= 'https://api.postcodes.io/postcodes?'
     response = requests.get(url,item)
     print(response.status_code)

     data = response.json()
     result = data.get('result', [])

     if result is None:
            return ['null']
     #Almacena cada codigo
     postcodes = [codes.get('postcode', 'N/A') for codes in result]
<<<<<<< HEAD
=======

     return postcodes,data


>>>>>>> develop

     return postcodes,data

