import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    #print(r.text)
    print(type(r.text))
    #Convertir en formato json para leerlo como lista
    categories = r.json() 
    for catogory in categories:
        print(catogory['name'])

