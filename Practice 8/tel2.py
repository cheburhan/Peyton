import psycopg2
import csv

try:
    conn = psycopg2.connect(
        host="localhost",
        database="phonebook_db",
        user="postgres",
        password="Samir_2007"
    )
    cursor = conn.cursor()
    print("успешно!")
except Exception as a:
    print("Ошибка подключения:", a)
    exit()

def add_contact_manual():
    name = input("Имя: ")
    phone = input("Телефон: ")
    cursor.execute("CALL add_or_update_contact(%s, %s)", (name, phone))  
    conn.commit()
    print("Контакт добавлен!")

def add_contact_csv():
    file_path = input("Путь к CSV: ")
    contacts_array = []
    
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                contacts_array.append([row[0], row[1]])
        
        cursor.execute("CALL add_many_contacts(%s)", (contacts_array,))  
        conn.commit()
        print("CSV добавлены!")
    except Exception as a:
        print("Ошибка", a)
        conn.rollback()

def update_contact():
    name = input("Новое имя: ")
    phone = input("Телефон контакта для обновления: ")
    cursor.execute("CALL add_or_update_contact(%s, %s)", (name, phone))  
    conn.commit()
    print("Контакт обновлён!")

def view_contacts():
    pattern = input("Поиск: ")
    cursor.execute("SELECT * FROM find_contacts(%s)", (pattern,))  
    rows = cursor.fetchall()
    if rows:
        print(f"\nНайдено контактов: {len(rows)}")
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Контакты не найдены.")

def view_paginated():
    limit = int(input("Сколько записей показать: "))
    offset = int(input("Сколько пропустить: "))
    cursor.execute("SELECT * FROM show_contacts_paginated(%s, %s)", (limit, offset))  
    rows = cursor.fetchall()
    print(f"\n=== Показано {len(rows)} записей ===")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    if rows:
        print(f"Всего записей в БД: {rows[0][3]}")

def delete_contact():
    print("Удалить по:")
    print("1 - Имени")
    print("2 - Телефону")
    choice = input("Выбор: ")
    value = input("Значение: ")
    
    if choice == '1':
        cursor.execute("CALL remove_contact(%s, %s)", ('name', value))  
    elif choice == '2':
        cursor.execute("CALL remove_contact(%s, %s)", ('phone', value))  
    else:
        print("Неверный выбор")
        return
    
    conn.commit()
    print("Контакт удалён!")

while True:
    print("\n-------------")
    print("1 - Добавить контакт вручную")
    print("2 - Добавить контакты из CSV")
    print("3 - Обновить контакт")
    print("4 - Поиск контактов")
    print("5 - Пагинация")
    print("6 - Удалить контакт")
    print("7 - Выход")
    
    choice = input("Действие: ")
    
    if choice == '1':
        add_contact_manual()
    elif choice == '2':
        add_contact_csv()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        view_contacts()
    elif choice == '5':
        view_paginated()
    elif choice == '6':
        delete_contact()
    elif choice == '7':
        print("До свидания!")
        break
    else:
        print("Неверный выбор")

cursor.close()
conn.close()