import requests
from plyer import notification
from src.shared.config import webhook
from src.shared.utils import check_null_data
from src.shared.log import logger

def send_discord_embed(row):
    embed = {
        "title": check_null_data(row["Naziv"]),
        "url": check_null_data(row["URL"]),
        "color": 16711738,
        "fields": [
            {"name": "Cena", "value": f"{check_null_data(row['Cena'])} €", "inline": True},
            {"name": "Registracija", "value": check_null_data(row['1.registracija']), "inline": True},
            {"name": "Kilometri", "value": check_null_data(row['Prevoženih']), "inline": True},
            {"name": "Motor", "value": check_null_data(row['Motor']), "inline": True}
        ],
        "footer": {"text": "Avto.net Scraper 🛠️"},
    }

    payload = {
        "embeds": [embed]
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(webhook['url'], json=payload, headers=headers)
        if response.status_code != 204 and response.status_code != 200:
            logger.warning(f"Failed to send embed to Discord: {response.status_code} - {response.text}")
        else:
            logger.info("Discord embed sent successfully.")
    except Exception:
        logger.exception("Exception occurred while sending embed to Discord.")

def send_discord_notifications(rows):
    for _, row in rows.iterrows():
        send_discord_embed(row)

def send_notification():
    try:
        notification.notify(
            title='New listing',
            message='A new car within your search parameters has been listed!',
            app_name='Avto-Net Scraper',
            timeout=10,
        )
        logger.info("Notification sent.")
    except Exception:
        logger.warning("Failed to send desktop notification.")