CREATE OR REPLACE FUNCTION search_user(pattern TEXT)
RETURNS TABLE(id INT, username TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM users
    WHERE username ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql; 

CREATE OR REPLACE PROCEDURE insert_or_update_user(username TEXT, phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM users WHERE username = insert_or_update_user.username) THEN
        UPDATE users SET phone = insert_or_update_user.phone
        WHERE username = insert_or_update_user.username;
    ELSE
        INSERT INTO users (username, phone) VALUES (insert_or_update_user.username, insert_or_update_user.phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_users(IN usernames TEXT[], IN phones TEXT[], OUT invalid_data TEXT)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
BEGIN
    invalid_data := '';
    WHILE i <= array_length(usernames, 1) LOOP
        IF phones[i] ~ '^\d{7,15}$' THEN
            CALL insert_or_update_user(usernames[i], phones[i]);
        ELSE
            invalid_data := invalid_data || '(' || usernames[i] || ', ' || phones[i] || '); ';
        END IF;
        i := i + 1;
    END LOOP;
END;
$$;

CREATE OR REPLACE FUNCTION get_users_paginated(lim INT, offs INT)
RETURNS TABLE(id INT, username TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM users ORDER BY id LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_user_by_username_or_phone(query TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM users
    WHERE username = query OR phone = query;
END;
$$;

