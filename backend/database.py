import mysql.connector
from mysql.connector import Error
from backend.config import Config

def get_connection():
    try:
        return mysql.connector.connect(**Config.DB_CONFIG)
    except Error as exc:
        raise RuntimeError(f"Unable to connect to MySQL: {exc}") from exc

class Database:
    @staticmethod
    def fetch_all(sql, params=()):
        conn=get_connection()
        try:
            cur=conn.cursor(dictionary=True)
            cur.execute(sql, params)
            return cur.fetchall()
        finally:
            cur.close(); conn.close()

    @staticmethod
    def fetch_one(sql, params=()):
        rows=Database.fetch_all(sql, params)
        return rows[0] if rows else None

    @staticmethod
    def execute(sql, params=(), commit=True):
        conn=get_connection()
        try:
            cur=conn.cursor()
            cur.execute(sql, params)
            if commit: conn.commit()
            return cur.lastrowid, cur.rowcount
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close(); conn.close()

    @staticmethod
    def transaction(callback):
        conn=get_connection()
        try:
            cur=conn.cursor(dictionary=True)
            result=callback(conn, cur)
            conn.commit()
            return result
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close(); conn.close()
