import sqlite3

conn = sqlite3.connect('shop.db')
cur = conn.cursor()

# таблица товаров
cur.execute('''
CREATE TABLE IN NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    image TEXT
    )
''')

# добавляем товары
cur.executemany('''
INSERT INTO products (name, description, price, image)
VALUES (?, ?, ?, ?) 
 ''', [
    ('Красные розы','небольшой букет вечной классики', 1500,'')
    ('Желтые тюльпаны','свежие, яркие тюльпына', 2500,'')
    ('Синие лилии','символ элегантности, изысканности и романтики', 3000,'')
])