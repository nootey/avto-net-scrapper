import requests
from datetime import datetime
from plyer import notification
from src.shared.config import webhook
from src.shared.utils import check_null_data

def send_discord_message(content):
    headers = {"Content-Type": "application/json"}
    data = {"content": content}
    response = requests.post(webhook['url'], headers=headers, json=data)
    if response.status_code != 204:
        print("Failed to send message:", response.text)

def send_discord_notifications(rows):
    for _, row in rows.iterrows():
        message = (
            f"**<-- NOV OGLAS 🚗 -->**\n"
            f"**AVTO:** {check_null_data(row['Naziv'])}\n"
            f"**CENA:** {check_null_data(row['Cena'])} €\n"
            f"**URL:** {check_null_data(row['URL'])}\n"
            f"**REGISTRACIJA:** {check_null_data(row['1.registracija'])}\n"
            f"**KILOMETRI:** {check_null_data(row['Prevoženih'])}\n"
            f"**MOTOR:** {check_null_data(row['Motor'])}"
        )
        send_discord_message(message)

def send_notification():
    notification.notify(
        title='Nova Objava',
        message='Nov avto je bil objavljen.',
        app_name='Avto-Net Scraper',
        timeout=10,
    )
