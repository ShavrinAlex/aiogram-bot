import sqlite3


db = sqlite3.connect('my_bot.db')
def execute(*args, **kwargs):
    cursor = db.cursor()
    cursor.execute(*args, **kwargs)
    db.commit()
    return cursor.fetchall()

def create_tables():
    """Функция создает таблицу и сохраняет её"""
    execute("""CREATE TABLE IF NOT EXISTS users(
        id BIGINT PRIMARY KEY NOT NULL,
        username TEXT,
        fullname TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'user',
        cash BIGINT NOT NULL    
    )""")
    db.commit()

def delete_tables():
    """Функция удаляет таблицу"""
    execute("DROP TABLE users")
    db.commit()

def see_tables():
    """Функция принтует таблицу"""
    for i in execute("SELECT * FROM users"):
        print(i)
