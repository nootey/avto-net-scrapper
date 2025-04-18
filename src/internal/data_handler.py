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

    merged = pd.merge(existing, new_cars, on='HASH', how='outer', indicator=True, suffixes=['_old', '_new'])
    diff = merged[merged['_merge'] != 'both']

    if diff.empty:
        logger.info("No new or removed car listings found.")
        return

    new_listings = diff[diff['_merge'] == 'right_only']

    if new_listings.empty:
        logger.info("No new listings to add.")
        return

    # Rebuild rows with only relevant columns
    new_listings_cleaned = new_listings.filter(regex='_new$|^HASH$').rename(columns=lambda col: col.replace('_new', ''))
    new_listings_cleaned = new_listings_cleaned[get_columns()]  # Reorder columns

    handle_data(new_listings_cleaned)

def handle_data(new_rows):
    existing = pd.read_csv('data/listings.csv', sep=';') if os.path.exists('data/listings.csv') else pd.DataFrame(columns=get_columns())
    updated = pd.concat([existing, new_rows], ignore_index=True)
    updated.to_csv('data/listings.csv', sep=';', index=False)

    if not new_rows.empty:
        logger.info(f"Found {len(new_rows)} new car listings.")
        send_discord_notifications(new_rows)
    else:
        logger.info("No new listings to add.")