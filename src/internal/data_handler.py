import pandas as pd
import os
from src.internal.notifier import send_discord_notifications
from src.shared.config import get_columns
from src.shared.log import logger

def compare_data(new_cars):
    try:
        existing = pd.read_csv('data/listings.csv', sep=';')
    except FileNotFoundError:
        existing = pd.DataFrame(columns=get_columns())

    merged = pd.merge(existing, new_cars, on='URL', how='outer', indicator=True, suffixes=['_old', '_new'])
    diff = merged[merged['_merge'] != 'both']

    if diff.empty:
        logger.info("No new or removed car listings found.")
        return

    if 'right_only' in diff['_merge'].values:
        diff = diff.filter(regex='_new$|^URL$').rename(columns=lambda x: x.replace('_new', ''))
        diff['action'] = 'new'
    else:
        diff = diff.filter(regex='_old$|^URL$').rename(columns=lambda x: x.replace('_old', ''))
        diff['action'] = 'delete'

    handle_data(diff)

def handle_data(diff):
    existing = pd.read_csv('data/listings.csv', sep=';') if os.path.exists('data/listings.csv') else pd.DataFrame(columns=get_columns())
    new_rows = diff[diff['action'] == 'new'].drop(columns='action')

    updated = pd.concat([existing, new_rows], ignore_index=True)
    updated.to_csv('data/listings.csv', sep=';', index=False)

    if not new_rows.empty:
        logger.info(f"Found {len(new_rows)} new car listings.")
        send_discord_notifications(new_rows)
    else:
        logger.info("No new listings to add.")