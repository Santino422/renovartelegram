import time
import requests
import os
from datetime import datetime

TOKEN_BOT = os.environ.get("8728841413:AAEu4_GofI0bXVv3wBfU2FMWP22VdBJvZls")
CHAT_ID   = os.environ.get("7096784407")

INTERVALO_MINUTOS      = 120
RENOVACIONES_POR_CICLO = 4

def enviar_telegram(mensaje):
    url  = f"https://api.telegram.org/bot{TOKEN_BOT}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "HTML"}
    try:
        requests.post(url, json=data)
        print(f"[{datetime.now().strftime('%H:%M')}] Mensaje enviado")
    except Exception as e:
        print(f"Error: {e}")

def ciclo_renovaciones():
    for i in range(1, RENOVACIONES_POR_CICLO + 1):
        hora    = datetime.now().strftime('%H:%M')
        mensaje = (
            f"⛏️ <b>Renovar servidor Minecraft</b>\n"
            f"📌 Renovación <b>{i}/{RENOVACIONES_POR_CICLO}</b>\n"
            f"🕐 Hora: {hora}\n"
            f"👉 ¡Entrá y renova!"
        )
        enviar_telegram(mensaje)
        if i < RENOVACIONES_POR_CICLO:
            print(f"Esperando {INTERVALO_MINUTOS} minutos...")
            time.sleep(INTERVALO_MINUTOS * 60)

print("Bot iniciado ✅")
enviar_telegram("🟢 Bot iniciado. Te aviso cada 120 minutos para renovar.")

while True:
    ciclo_renovaciones()
    time.sleep(INTERVALO_MINUTOS * 60)