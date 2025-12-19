import requests
import os
from dotenv import load_dotenv

load_dotenv()

def obtener_datos_jugador():
    api_key = os.getenv("API_KEY")

    
    if not api_key:
        print("❌ Error: Faltan datos en el .env")
        return

    headers = { "Authorization": api_key }

    # PASO 0: Solicitamos datos al usuario

    nombre = input("Por favor escribe el nombre del jugador: ")
    tag = input("Por favor escribe el tag del jugador: ")

    # PASO 1: Obtenemos datos de la cuenta (Nivel, Región, Foto)
    print(f"📡 1. Buscando perfil de {nombre}#{tag}...")
    url_account = f"https://api.henrikdev.xyz/valorant/v1/account/{nombre}/{tag}"
    resp_account = requests.get(url_account, headers=headers)

    if resp_account.status_code != 200:
        print(f"❌ Error al buscar cuenta: {resp_account.status_code}")
        return

    data_acc = resp_account.json()['data']
    region = data_acc['region']  # Guardamos la región (ej: na, latam, eu)
    
    # PASO 2: Con la región, buscamos el Rango (MMR)
    print(f"📡 2. Buscando rango en servidor {region.upper()}...")
    url_mmr = f"https://api.henrikdev.xyz/valorant/v1/mmr/{region}/{nombre}/{tag}"
    resp_mmr = requests.get(url_mmr, headers=headers)

    # Preparamos el texto del rango
    rango_texto = "Unranked / No disponible"
    elo = 0
    
    if resp_mmr.status_code == 200:
        data_mmr = resp_mmr.json()['data']
        # 'currenttierpatched' nos da el nombre bonito (ej: Gold 3)
        rango_texto = data_mmr.get('currenttierpatched', 'Desconocido')
        elo = data_mmr.get('ranking_in_tier', 0)

    # IMPRIMIR RESULTADOS
    print("\n✅ ¡DATOS COMPLETOS!")
    print("=================================")
    print(f"🆔 Cuenta: {data_acc['name']} #{data_acc['tag']}")
    print(f"🌎 Región: {region.upper()}")
    print(f"💯 Nivel:  {data_acc['account_level']}")
    print("---------------------------------")
    print(f"🏆 Rango:  {rango_texto}")
    print(f"📈 RR:     {elo}/100")
    print("---------------------------------")
    print(f"🖼️ Card:   {data_acc['card']['small']}")
    print("=================================")

if __name__ == "__main__":
    obtener_datos_jugador()