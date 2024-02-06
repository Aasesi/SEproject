import sqlite3
import hashlib


class UserDatabaseSQL:
    def __init__(self, db_name='medical_database.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        if not self.conn:
            self.connect()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS logins (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT,
                usertype TEXT,
                name TEXT,
                surname TEXT
            )
        ''')

    def validate(self, username, password):
        self.connect()
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        self.cursor.execute('''
                    SELECT COUNT(*) FROM logins
                    WHERE username = ? AND password = ?
                ''', (username, hashed_password))

        result = self.cursor.fetchone()[0]

        self.commit_and_close()

        return result > 0

    def add_user(self, name, surname, role, username, password):
        self.connect()
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        self.cursor.execute('''
                    INSERT INTO logins (username, password, usertype, name, surname)
                    VALUES (?, ?, ?, ?, ?)
                ''', (username, hashed_password, role, name, surname))

        self.commit_and_close()
        print("Register Complete")

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()

    def delete_user(self, name, surname):
        self.connect()
        self.cursor.execute('''
                    DELETE FROM logins
                    WHERE name = ? AND surname = ?
                ''', (name, surname))
        self.commit_and_close()

    def update_user_data(self, username, new_password):
        self.connect()
        hashed_password = hashlib.sha256(new_password.encode('utf-8')).hexdigest()

        self.cursor.execute('''
                    UPDATE logins
                    SET password = ?
                    WHERE username = ?
                ''', (hashed_password, username))

        self.commit_and_close()

    def get_current_user(self, username, password):
        self.connect()
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.cursor.execute('''
        SELECT name, surname, usertype FROM logins
        WHERE username = ? AND password = ? 
        ''', (username, hashed_password))

        result = self.cursor.fetchall()
        return result
