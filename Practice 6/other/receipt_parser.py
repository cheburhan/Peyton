import re
import json
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Extract all prices

price_pattern = r'\d[\d\s]*,\d{2}'
prices = re.findall(price_pattern, text)

# преобразуем цены в числа
def normalize_price(p):
    p = p.replace(" ", "").replace(",", ".")
    return float(p)

price_values = [normalize_price(p) for p in prices]



# 2. Find product names

product_pattern = r'\d+\.\n([^\n]+)'
products = re.findall(product_pattern, text)



# 3. Calculate total amount

total_pattern = r'ИТОГО:\s*\n?([\d\s,]+)'
total_match = re.search(total_pattern, text)

total = None
if total_match:
    total = normalize_price(total_match.group(1))



# 4. Extract date and time

datetime_pattern = r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})'
datetime_match = re.search(datetime_pattern, text)

date = None
time = None

if datetime_match:
    date = datetime_match.group(1)
    time = datetime_match.group(2)



# 5. Payment method
payment_pattern = r'(Банковская карта|Наличные)'
payment_match = re.search(payment_pattern, text)

payment_method = payment_match.group(1) if payment_match else None



# 6. Structured Output

data = {
    "products": products,
    "prices": price_values,
    "total": total,
    "payment_method": payment_method,
    "date": date,
    "time": time
}

print(json.dumps(data, indent=4, ensure_ascii=False))