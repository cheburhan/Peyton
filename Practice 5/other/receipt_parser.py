import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Функция для нормализации цен
def normalize_price(p):
    # Сначала убираем пробелы, затем заменяем запятую на точку
    p = p.replace(" ", "").replace(",", ".")
    # Убираем возможные переносы строк
    p = p.replace("\n", "")
    return float(p)

# 1. Extract all prices from the receipt
price_pattern = r'\d+(?:\s*\d+)*,\d{2}'
prices = re.findall(price_pattern, text)

# Альтернативный подход: сначала убрать переносы строк между цифрами
text_fixed = re.sub(r'(\d)\n(\d)', r'\1\2', text)
prices = re.findall(r'\d[\d\s]*,\d{2}', text_fixed)

price_values = [normalize_price(p) for p in prices]

# 2. Find all product names
product_pattern = r'\d+\.\n([^\n]+)'
products = re.findall(product_pattern, text)

# Очистка имен продуктов
products = [p.strip() for p in products]

# 3. Calculate total amount
total_pattern = r'ИТОГО:\s*\n?([\d\s,]+)'
total_match = re.search(total_pattern, text)
total = normalize_price(total_match.group(1)) if total_match else None

# 4. Extract date and time information
datetime_pattern = r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})'
datetime_match = re.search(datetime_pattern, text)

date = datetime_match.group(1) if datetime_match else None
time = datetime_match.group(2) if datetime_match else None

# 5. Find payment method
payment_pattern = r'(Банковская карта|Наличные)'
payment_match = re.search(payment_pattern, text)
payment_method = payment_match.group(1) if payment_match else None

# 6. Create a structured output
data = {
    "products": products,
    "prices": price_values,
    "total": total,
    "payment_method": payment_method,
    "date": date,
    "time": time
}

# Вывод
print("=== ПАРСИНГ ЧЕКА ===\n")
print(f"Дата и время: {date} {time}")
print(f"Способ оплаты: {payment_method}")
print(f"Общая сумма: {total:.2f} тенге\n")
print("Товары:")
for i, (product, price) in enumerate(zip(products, price_values), 1):
    print(f"{i:2d}. {product[:40]:40} {price:8.2f}")

print("\n=== JSON OUTPUT ===")
print(json.dumps(data, indent=4, ensure_ascii=False))