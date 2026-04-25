-- 1. Функция для поиска 
CREATE OR REPLACE FUNCTION find_contacts(pattern TEXT)
RETURNS TABLE(
    id INT,
    first_name VARCHAR,
    phone VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.phone
    FROM phonebook p
    WHERE p.first_name ILIKE '%' || pattern || '%'
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 4. Функция для пагинации 
CREATE OR REPLACE FUNCTION show_contacts_paginated(
    p_limit INT,
    p_offset INT
)
RETURNS TABLE(
    id INT,
    first_name VARCHAR,
    phone VARCHAR,
    total_count BIGINT
) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.first_name, p.phone,
           (SELECT COUNT(*) FROM phonebook) as total_count
    FROM phonebook p
    ORDER BY p.id
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
