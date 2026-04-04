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
    print("Подключение к базе успешно!")
except Exception as e:
    print("Ошибка подключения:", e)
    exit()

def add_contact_manual():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    #отправка sql запроса
    cursor.execute(
        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit() #сохранение изменения в базе, без нее данные будут просто висеть в памяти
    print("Контакт добавлен!")

def add_contact_csv():
    file_path = input("Введите путь к CSV файлу: ")
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  #пропустить заголовок
            for row in reader:
                cursor.execute(
                    "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
        conn.commit()
        print("Контакты из CSV добавлены!")
    except Exception as e:
        print("Ошибка при работе с CSV:", e)

def update_contact():
    choice = input("Что хотите изменить? 1-Имя, 2-Телефон: ")
    if choice == '1':
        old_phone = input("Введите телефон контакта: ")
        new_name = input("Введите новое имя: ")
        cursor.execute(
            "UPDATE phonebook SET first_name=%s WHERE phone=%s",
            (new_name, old_phone)
        )
    elif choice == '2':
        old_name = input("Введите имя контакта: ")
        new_phone = input("Введите новый телефон: ")
        cursor.execute(
            "UPDATE phonebook SET phone=%s WHERE first_name=%s",
            (new_phone, old_name)
        )
    conn.commit()
    print("Контакт обновлён!")

def view_contacts():
    filter_choice = input("Фильтр? 1-Все, 2-По имени, 3-По телефону: ")
    if filter_choice == '1':
        cursor.execute("SELECT * FROM phonebook")
    elif filter_choice == '2':
        name = input("Введите имя для поиска: ")
        cursor.execute("SELECT * FROM phonebook WHERE first_name LIKE %s", (f"%{name}%",))
    elif filter_choice == '3':
        phone = input("Введите телефон для поиска: ")
        cursor.execute("SELECT * FROM phonebook WHERE phone=%s", (phone,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Контакты не найдены.")

def delete_contact():
    choice = input("Удалить по: 1-Имя, 2-Телефон: ")
    if choice == '1':
        name = input("Введите имя: ")
        cursor.execute("DELETE FROM phonebook WHERE first_name=%s", (name,))
    elif choice == '2':
        phone = input("Введите телефон: ")
        cursor.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
    conn.commit()
    print("Контакт удалён!")

def delete_all():
    cursor.execute("DELETE FROM phonebook")
    conn.commit()
    print("Все удалено!")

while True:
    print("\n--- PhoneBook ---")
    print("1 - Добавить контакт вручную")
    print("2 - Добавить контакты из CSV")
    print("3 - Обновить контакт")
    print("4 - Просмотреть контакты")
    print("5 - Удалить контакт")
    print("6 - Выход")
    print("7 - ВООБЩЕ ВСЕ СНЕСТИ")
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
        delete_contact()
    elif choice == '6':
        print("Ну все")
    elif choice == '7':
        delete_all()
        break
    else:
        print("Неверный выбор, попробуйте снова.")

cursor.close()
conn.close()