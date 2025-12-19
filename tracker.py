import requests
import os
from dotenv import load_dotenv

load_dotenv()

# CAMBIO CLAVE:
# 1. Cambiamos el nombre a 'obtener_rango'
# 2. Ahora recibe (nombre, tag) desde la ventana, NO usa input()
def obtener_rango(nombre, tag):
    api_key = os.getenv("API_KEY")
    
    if not api_key:
        return "❌ Error: Falta API KEY en .env"

    headers = { "Authorization": api_key }

    # 1. Buscando perfil
    url_account = f"https://api.henrikdev.xyz/valorant/v1/account/{nombre}/{tag}"
    resp_account = requests.get(url_account, headers=headers)

    if resp_account.status_code != 200:
        return f"❌ No se encontró a {nombre}#{tag}"

    data_acc = resp_account.json()['data']
    region = data_acc['region']
    
    # 2. Buscando rango
    url_mmr = f"https://api.henrikdev.xyz/valorant/v1/mmr/{region}/{nombre}/{tag}"
    resp_mmr = requests.get(url_mmr, headers=headers)

    if resp_mmr.status_code == 200:
        data_mmr = resp_mmr.json()['data']
        rango = data_mmr.get('currenttierpatched', 'Unranked')
        elo = data_mmr.get('ranking_in_tier', 0)
        nivel = data_acc['account_level']
        
        return f"Región: {region.upper()} | Nivel: {nivel}\n\n{rango}\n{elo} RR"
    
    return "No se pudo obtener el rango."
