import sqlite3

def create_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, author TEXT, ISBN INTEGER)")
    conn.commit()
    conn.close()

def insert(title, year, author, isbn):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?, ?)", (title, year, author, isbn))
    conn.commit()
    conn.close()

def view_all():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id, ))
    conn.commit()
    conn.close()

def update(id, title, year, author, isbn):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE books  SET title=?, year =?, author = ?, ISBN = ? WHERE id =?", (title, year, author, isbn,  id,))
    conn.commit()
    conn.close()

def search(title='', year='', author='', isbn=''):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year=? OR ISBN =?",(title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

create_table()
