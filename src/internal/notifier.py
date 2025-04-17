import requests
from plyer import notification
from src.shared.config import webhook
from src.shared.utils import check_null_data
from src.shared.log import logger

def send_discord_message(content):
    headers = {"Content-Type": "application/json"}
    data = {"content": content}

    try:
        response = requests.post(webhook['url'], headers=headers, json=data)
        if response.status_code != 204:
            logger.warning(f"Failed to send message to Discord: {response.text}")
        else:
            logger.info("Discord message sent successfully.")

    except Exception as e:
        logger.exception("Exception occurred while sending message to Discord.")

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
    try:
        notification.notify(
            title='Nova Objava',
            message='Nov avto je bil objavljen.',
            app_name='Avto-Net Scraper',
            timeout=10,
        )
        logger.info("Local desktop notification sent.")

    except Exception as e:
        logger.warning("Failed to send desktop notification.")
