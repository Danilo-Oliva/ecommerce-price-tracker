#Titulo del producto: <h1 class="ui-pdp-title"
#Precio: <Span class="andes-money-amount__fraction"
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import csv

os.system("cls")


headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

respuesta = requests.get("https://www.mercadolibre.com.ar/auriculares-nothing-ear-a-bluetooth-53-con-cancelacion-de-ruido-de-45-db-integracion-con-chat-gpt-audio-hi-res-color-blanco/p/MLA38365682#reco_item_pos=3&reco_backend=item_decorator&reco_backend_type=function&reco_client=home_items-decorator-legacy&reco_id=f0d60d7b-05d9-4200-b1da-978da6da1dfc&reco_model=&c_id=/home/navigation-recommendations-seed/element&c_uid=f310f6ec-2f22-4f6e-8091-40655fe92052&da_id=navigation&da_position=4&id_origin=/home/dynamic_access&da_sort_algorithm=ranker", headers=headers)
  
sopa = BeautifulSoup(respuesta.content, 'html.parser')

etiqueta_titulo = sopa.find("h1", class_="ui-pdp-title")
etiqueta_precio = sopa.find("span", class_="andes-money-amount__fraction")
texto_titulo = etiqueta_titulo.get_text(strip=True)

#data cleaning
precio = etiqueta_precio.get_text(strip=True).replace('.', '')

precio = int(precio)

#extraemos hora
fecha_de_scraping = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#guardamos hora
with open("precios.csv", "a", newline='') as archivo_precios:
  escritor = csv.writer(archivo_precios)
  escritor.writerow([fecha_de_scraping, texto_titulo, precio])


print(texto_titulo)


if precio < 180000:
  print(f"\nOferta!Comprar ya. Precio: ${precio}")
else:
  print(f"\nSeguir esperando. Precio: {precio}")

print(f"Fecha = {fecha_de_scraping}")