--  Процедура upsert 
CREATE OR REPLACE PROCEDURE add_or_update_contact(
    p_first_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE phone = p_phone) THEN
        UPDATE phonebook 
        SET first_name = p_first_name
        WHERE phone = p_phone;
    ELSE
        INSERT INTO phonebook (first_name, phone) 
        VALUES (p_first_name, p_phone);
    END IF;
END;
$$;

--  Процедура для массовой вставки 
CREATE OR REPLACE PROCEDURE add_many_contacts(
    contacts_data TEXT[][]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    first_name VARCHAR;
    phone VARCHAR;
    invalid_data TEXT := '';
BEGIN
    FOR i IN 1..array_length(contacts_data, 1) LOOP
        first_name := contacts_data[i][1];
        phone := contacts_data[i][2];
        
        IF phone ~ '^\+[0-9]{10,15}$' THEN
            CALL add_or_update_contact(first_name, phone);
        ELSE
            invalid_data := invalid_data || format('Неверный телефон: %s (Имя: %s)\n', 
                                                   phone, first_name);
        END IF;
    END LOOP;
    
    IF invalid_data <> '' THEN
        RAISE EXCEPTION 'Некорректные данные:\n%', invalid_data;
    END IF;
END;
$$;



--  Процедура для удаления 
CREATE OR REPLACE PROCEDURE remove_contact(
    delete_by VARCHAR,
    value VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF delete_by = 'name' THEN
        DELETE FROM phonebook WHERE first_name = value;
    ELSIF delete_by = 'phone' THEN
        DELETE FROM phonebook WHERE phone = value;
    ELSE
        RAISE EXCEPTION 'Параметр delete_by должен быть "name" или "phone"';
    END IF;
END;
$$;

-- Проверка новых объектов
SELECT 
    proname as "Имя",
    CASE 
        WHEN prokind = 'f' THEN 'Функция'
        WHEN prokind = 'p' THEN 'Процедура'
    END as "Тип"
FROM pg_proc 
WHERE proname IN ('find_contacts', 'add_or_update_contact', 'add_many_contacts', 'show_contacts_paginated', 'remove_contact');