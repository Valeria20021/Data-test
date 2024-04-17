import requests


def get_postcode():
    #url= 'https://api.postcodes.io/outcodes?'
    r = requests.get('https://api.postcodes.io/outcodes?lat=54,687055&lon=-1,241763')

    print(r.status_code)
    print(r.text)

    data = r.json()
    postcodes = data.get('result', [])
    for codes in postcodes:
        outcode = codes.get('outcode', 'N/A')
        print("Outcode:", outcode)

