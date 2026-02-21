# Импортируем встроенный модуль для работы с JSON
import json

# Открываем файл sample-data.json в режиме чтения
with open("sample-data.json") as f:
    
    # Загружаем JSON из файла и превращаем его в словарь Python
    data = json.load(f)

# Печатаем заголовок таблицы
print("Interface Status")

# Печатаем линию из 80 символов "="
print("=" * 80)

# Форматируем и печатаем названия колонок
# :50 означает — выделить 50 символов под колонку
print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")

# Печатаем разделительную линию
print("-" * 80)

# Проходим по каждому элементу списка imdata
for item in data["imdata"]:
    
    # Заходим внутрь словаря l1PhysIf, затем в attributes
    attr = item["l1PhysIf"]["attributes"]
    
    # Достаём значение поля dn
    dn = attr["dn"]
    
    # Достаём значение скорости
    speed = attr["speed"]
    
    # Достаём значение MTU
    mtu = attr["mtu"]
    
    # Печатаем строку таблицы с форматированием колонок
    # dn:50 — 50 символов
    # '':20 — пустая колонка Description (20 символов)
    # speed:8 — 8 символов
    # mtu:6 — 6 символов
    print(f"{dn:50} {'':20} {speed:8} {mtu:6}")
