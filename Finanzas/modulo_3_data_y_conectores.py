# -*- coding: utf-8 -*-
"""Modulo 3 : Data y Conectores

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tFtEUBBVs8hY81Cha9VK2TcZ13V3NA0y
"""

# Ejemplo en regres
import requests

#diccionario = requests.get("https://reqres.in/api/users?page=2").json()

# diccionario["data"][0]["first_name"]

BASE_URL = "https://reqres.in/api/"
parameters = {"page":2}
diccionario = requests.get (f"{BASE_URL}users", params = parameters).json()
diccionario

# Ejemplo en regres
import requests

#diccionario = requests.get("https://reqres.in/api/users?page=2").json()

# diccionario["data"][0]["first_name"]
id = 2
BASE_URL = "https://reqres.in/"
response = requests.get (f"{BASE_URL}api/users/{id}").json()
response

# POST

import requests

body = {
    "name": "morpheus",
    "job": "leader"
}

#requests.post(f"{BASE_URL}api/users", data= body).text
response = requests.post(f"{BASE_URL}api/users", data= body).json()
response

# PUT modificacion, pasa todo el recurso

import requests

body = {
    "name": "morpheus",
    "job": "zion resident"
}

url = "https://reqres.in/api/users/2"

requests.put(url , data = body ).json()

# Delete (lo de arriba)

requests.delete(url)

# Conectarse a API IOL.
# https://www.invertironline.com/api

"""

https://api.invertironline.com/token
POST /token HTTP/1.1
Host: api.invertironline.com
Content-Type: application/x-www-form-urlencoded
username=MIUSUARIO&password=MICONTRASEÑA&grant_type=password

"""

import requests

MIUSUARIO = "agvanetta@gmail.com"
PASS = "racingclub2"

h = {
    "Content-Type":"application/x-www-form-urlencoded"
}
body = {
    "username" : MIUSUARIO,
    "password" : PASS,
    "grant_type" : "password"
}

base_url = "https://api.invertironline.com"

response = requests.post(base_url + "/token", headers=h, data= body).json()
print(response)

import pandas as pd

pd.DataFrame(data)

# Market Data

def obtener_token():
  import requests
  MIUSUARIO = "agvanetta@gmail.com"
  PASS = "racingclub2"
  h = {
      "Content-Type":"application/x-www-form-urlencoded"
  }
  body = {
      "username" : MIUSUARIO,
      "password" : PASS,
      "grant_type" : "password"
  }
  base_url = "https://api.invertironline.com"
  response = requests.post(base_url + "/token", headers=h, data= body).json()
  token = response["access_token"]
  return token

#Market Data documentacion : https://api.invertironline.com/
obtener_token()

# RUTA

import requests

mercado =  "bCBA"
simbolo = "GGAL"
fechaDesde = "2019-01-01"
fechaHasta = "2022-01-01"
ajustada = "sinAjustar"
base_url = "https://api.invertironline.com"
ruta = f"/api/v2/{mercado}/Titulos/{simbolo}/Cotizacion/seriehistorica/{fechaDesde}/{fechaHasta}/{ajustada}"
api_token = obtener_token()

h = {
    "Authorization": "Bearer " + api_token
}

data = requests.get(base_url + ruta, headers = h).json()

# Fondos comunes de inversion
#https://api.invertironline.com/#/

import requests
api_token = obtener_token()
headers = {
    "Authorization": "Bearer " + api_token
}

endpoint = base_url + "/api/v2/Titulos/FCI"

FCI = requests.get(endpoint, headers = headers ).json()
FCI

import pandas as pd

df = pd.DataFrame(FCI)
df.to_excel("FCIs.xlsx")

import requests
pais = "argentina"
endpoint = base_url + f"/api/v2/{pais}/Titulos/Cotizacion/Instrumentos"
requests.get(endpoint, headers = headers).json()

import requests

pais = "argentina"
instrumento = "Acciones"
endpoint = base_url + f"/api/v2/{pais}/Titulos/Cotizacion/Paneles/{instrumento}"


requests.get(endpoint, headers = headers).json()

import requests

Pais = "argentina"
Instrumento = "Acciones"
Panel = "CEDEARs"

endpoint = base_url + f"/api/v2/Cotizaciones/{Instrumento}/{Panel}/{Pais}"

requests.get(endpoint, headers = headers ).json()

from pandas.core.arrays import base
# Estado de cuenta

path = "/api/v2/estadocuenta"
endpoint = base_url + path

dataCuenta = requests.get( endpoint , headers = headers ).json()
dataCuenta

# Portafolio

pais = "argentina"
pathPortafolio = f"/api/v2/portafolio/{pais}"
endpoint = base_url + pathPortafolio

requests.get(endpoint , headers = headers ).json()



##########################################ACTIVARTOKEN##########################################

api_token = obtener_token()
headers = {
    "Authorization": "Bearer " + api_token
}

################################################################################################

# Ruteo de ordenes

Simbolo = "TSLA"
Mercado = "bCBA"

endpoint = f"{base_url}/api/v2/{Mercado}/Titulos/{Simbolo}/Cotizacion"

data = requests.get ( url = endpoint , headers = headers).json()
data
cantidad_venta = data["puntas"][0]['cantidadVenta']
cantidad_compra = data["puntas"][0]['precioVenta']

"""Compra"""

import datetime as dt
vigencia = dt.datetime.now() + dt.timedelta(days=1)
vigencia_str = dt.datetime.strftime(vigencia, '%Y-%m-%d')

ticker = "COME"
cantidad = 1 
precio =  3
plazo = "t2"
params = {
  "mercado": "bCBA",
  "simbolo": ticker,
  "cantidad": cantidad,
  "precio": precio,
  "plazo": plazo,
  "validez": vigencia_str
}


endpoint = base_url + '/api/v2/operar/Comprar/'

#ata = requests.post(endpoint, headers = headers, data = params).json()
#data

#devuelve un numero de operacion

"""Cancelar orden"""

nro_operacion = data["numeroOperacion"]
requests.get(BASE_URL+f"/api/v2/operaciones/{nro_operacion}", headers = headers).json()