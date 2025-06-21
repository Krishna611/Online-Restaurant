import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS menu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    address TEXT,
    status TEXT DEFAULT 'Cooking'
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    menu_item_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(menu_item_id) REFERENCES menu(id)
)
''')

c.executemany("INSERT INTO menu (name, price) VALUES (?, ?)", [
    ('Non-Veg Starters', 200),
    ('Veg Starters', 150),
    ('Soups', 120),
    ('Fish & Sea food', 300),
    ('Main Course', 250),
    ('Noodles', 180),
    ('Salads', 100),
    ('Desserts', 90)
])

conn.commit()
conn.close()
print("Database initialized")
