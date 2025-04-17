import re
from src.shared.log import logger

def extract_property(result, property_class, tag_type):
    try:
        el = result.find(tag_type, class_=property_class)
        if tag_type == 'a':
            return el['href']
        return el.text.strip()
    except (AttributeError, TypeError, KeyError):
        return None

def collect_car_data(text_block):
    lines = [line.strip() for line in text_block.split('\n') if line.strip()]
    if len(lines) % 2 != 0:
        lines = lines[:-1]
    return {lines[i]: lines[i+1] for i in range(0, len(lines), 2)}

def format_price(price):
    match = re.search(r"[\d,.]+(?=\s*€)", price)
    return match.group().replace(".", "").replace(",", "") if match else ""

def check_null_data(value):
    return ":x:" if value is None else str(value)
