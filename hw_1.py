import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname="second",
        user="postgres",
        password="Aa1234",
        host="localhost",
        port="5432"
    )


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL
                );
            """)
            conn.commit()
    print("Таблица создана!")


def create_user(name, email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("BEGIN;")
            cur.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
                (name, email)
            )
            user_id = cur.fetchone()[0]
            conn.commit()
    print(f"Пользователь создан с id: {user_id}")


def read_all_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users;")
            users = cur.fetchall()
    return users


def read_user(user_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
            user = cur.fetchone()
    return user


def update_user(user_id, new_name, new_email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("BEGIN;")
            cur.execute(
                "UPDATE users SET name = %s, email = %s WHERE id = %s RETURNING id;",
                (new_name, new_email, user_id)
            )
            updated_id = cur.fetchone()
            conn.commit()
    if updated_id:
        print(f"Пользователь с id {user_id} обновлен.")
    else:
        print("Ошибка: Пользователь не найден!")


def delete_user(user_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("BEGIN;")
            cur.execute("DELETE FROM users WHERE id = %s RETURNING id;", (user_id,))
            deleted_id = cur.fetchone()
            conn.commit()
    if deleted_id:
        print(f"Пользователь с id {user_id} удален.")
    else:
        print("Ошибка: Пользователь не найден!")


if __name__ == "__main__":
    create_table()

    create_user("Иван Иванов", "ivan@example.com")
    create_user("Анна Смирнова", "anna@example.com")

    users = read_all_users()
    print("Все пользователи:", users)

    user = read_user(1)
    print("Один пользователь:", user)

    update_user(1, "Иван Петров", "ivan.petrov@example.com")

    delete_user(2)

    users = read_all_users()
    print("Пользователи после удаления:", users)
