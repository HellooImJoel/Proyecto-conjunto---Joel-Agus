#main project

import requests
from bs4 import BeautifulSoup

# URL del producto que quieres rastrear
url = 'https://www.mercadolibre.com.ar/bicicleta-silverfox-r29-21v-mtb-aluminio-29-freno-disco-susp-color-naranja-tamano-del-cuadro-18/p/MLA23755521?pdp_filters=seller_id%3A70513647#reco_item_pos=1&reco_backend=machinalis-seller-items-pdp&reco_backend_type=low_level&reco_client=pdp-seller_items-above&reco_id=79845acc-7aff-4267-af41-c6ee49a53d2e'

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




