import sqlite3

conn = sqlite3.connect('MenuStore/menu.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        ingredients TEXT NOT NULL
    )
''')

cursor.execute("INSERT INTO menu_items (name, price, ingredients) VALUES ('Metric Ton Bacon Burger', 120, 'Bacon, Cheddar, Lök')")
cursor.execute("INSERT INTO menu_items (name, price, ingredients) VALUES ('Demure Chicken', 85, 'Kyckling, Tomat, Sallad')")
cursor.execute("INSERT INTO menu_items (name, price, ingredients) VALUES ('Cutie Veggie', 75, 'Vegansk biff, Sallad, Tomat')")

cursor.execute("INSERT INTO menu_items (name, price, ingredients) VALUES ('Pommes Frites', 30, 'Friterad potatis')")
cursor.execute("INSERT INTO menu_items (name, price, ingredients) VALUES ('Fanta', 20, 'Kolsyra, Apelsinsmak')")


conn.commit()
conn.close()
