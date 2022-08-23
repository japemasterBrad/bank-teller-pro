import sqlite3 as sql

class Categories:
    def __init__(self):
        conn = sql.connect("./db/categories.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS categories("
                    "cat_id INT PRIMARY KEY NOT NULL,"
                    "cat_name VARCHAR(50) NOT NULL,"
                    "cat_hex_code VARCHAR(7) NOT NULL"
                    ")"
                    )
        conn.commit()
        conn.close()
        
        print("Loaded Categories")
        
    def addNewCategory(self, cat_name, cat_hex_code):
        conn = sql.connect("./db/categories.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO categories VALUES ((?) (?) (?))",
                    (None, cat_name, cat_hex_code)
                    )
        conn.commit()
        conn.close()
        
        