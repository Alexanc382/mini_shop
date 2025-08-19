import sqlite3

conn = sqlite3.connect('new_shop.db')
cur = conn.cursor()

# таблица товаров
cur.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    image TEXT
    )
''')

# добавлены товары
cur.executemany('''
INSERT INTO products (name, description, price, image)
VALUES (?, ?, ?, ?) 
 ''', [
    ('Красные розы','небольшой букет вечной классики', 7500,'images/red_roses.jpg'),
    ('Желтые тюльпаны','свежие, яркие тюльпына', 6500,'images/yellow_tulips.jpeg'),
    ('Синие лилии','символ элегантности, изысканности и романтики', 9000,'images/blue_lilies.jpg')
])

conn.commit()
conn.close()

print('База данных создана')