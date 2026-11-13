
from getpass import getpass
from werkzeug.security import generate_password_hash
from backend.database import get_connection


def create_admin():
    username = input("Admin username: ").strip()
    full_name = input("Full name: ").strip()
    email = input("Email: ").strip() or None

    password = getpass("Admin password: ")
    confirm = getpass("Confirm password: ")

    if not username or not full_name or not password:
        print("Please fill all required fields.")
        return

    if password != confirm:
        print("Passwords do not match.")
        return

    if len(password) < 8:
        print("Password must be at least 8 characters.")
        return

    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        cur.execute("""
            SELECT role_id FROM roles
            WHERE role_code = 'ADMIN' AND is_active = 1
        """)
        role = cur.fetchone()

        if not role:
            print("Admin role not found.")
            return

        cur.execute("""
            SELECT user_id FROM users
            WHERE username = %s OR (email = %s AND email IS NOT NULL)
        """, (username, email))

        if cur.fetchone():
            print("Username or email already exists.")
            return

        password_hash = generate_password_hash(password)

        cur.execute("""
            INSERT INTO users
            (username, password_hash, full_name, email, role_id, status)
            VALUES (%s, %s, %s, %s, %s, 'ACTIVE')
        """, (username, password_hash, full_name,
              email, role["role_id"]))

        conn.commit()
        print("Admin account created successfully!")

    except Exception as error:
        if conn:
            conn.rollback()
        print("Error:", error)

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    create_admin()
