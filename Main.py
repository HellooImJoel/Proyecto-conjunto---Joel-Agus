#main project

import requests
from bs4 import BeautifulSoup

# URL del producto que quieres rastrear
url = 'https://www.mercadolibre.com.ar/bicicleta-sunny-modelo-mtl-290-rodado-29-negro-naranja-color-negronaranja-tamano-del-cuadro-m/p/MLA17921665?product_trigger_id=MLA17921666&quantity=1'

headers = {
    "User-Agent": "Edge/91.0.4472.124 Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

"""
def check_price():
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra el precio del producto en la página web
    # (esto puede variar dependiendo de la estructura de la página web)
    price = soup.find("span", attrs={"class":'andes-money-amount__fraction'}).string 

    print(price)
""" 
def check_price():
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra el precio del producto en la página web
    price = soup.find("span", attrs={"class":'andes-money-amount__fraction'}).string 

    print(price)

check_price()





