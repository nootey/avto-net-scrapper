import pandas as pd
import os
from src.internal.notifier import send_discord_notifications

columns = ['URL', 'Cena', 'Naziv', '1.registracija', 'Prevoženih', 'Menjalnik','Motor']

def compare_data(new_cars):
    try:
        existing = pd.read_csv('data/listings.csv', sep=';')
    except FileNotFoundError:
        existing = pd.DataFrame(columns=columns)

    merged = pd.merge(existing, new_cars, on='URL', how='outer', indicator=True, suffixes=['_old', '_new'])
    diff = merged[merged['_merge'] != 'both']

    if diff.empty:
        return

    if 'right_only' in diff['_merge'].values:
        diff = diff.filter(regex='_new$|^URL$').rename(columns=lambda x: x.replace('_new', ''))
        diff['action'] = 'new'
    else:
        diff = diff.filter(regex='_old$|^URL$').rename(columns=lambda x: x.replace('_old', ''))
        diff['action'] = 'delete'

    handle_data(diff)

def handle_data(diff):
    existing = pd.read_csv('data/listings.csv', sep=';') if os.path.exists('data/listings.csv') else pd.DataFrame(columns=columns)
    new_rows = diff[diff['action'] == 'new'].drop(columns='action')

    existing = pd.concat([existing, new_rows], ignore_index=True)
    existing.to_csv('data/listings.csv', sep=';', index=False)

    if not new_rows.empty:
        send_discord_notifications(new_rows)