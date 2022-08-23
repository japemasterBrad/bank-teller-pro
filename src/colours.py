import sqlite3 as sql

class Colours:
    def __init__(self):
        conn = sql.connect("./db/colours.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS colours("
                    "col_id INT PRIMARY KEY NOT NULL,"
                    "col_name VARCHAR(50) NOT NULL,"
                    "col_hex VARCHAR(7) NOT NULL"
                    ")"
                    )
        conn.commit()
        conn.close()
        
    def add_new_colour(self, name, hex_value):
        conn = sql.connect("./db/colours.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO colours VALUES ((?) (?)))", (None, name, hex_value)
                    )
        conn.commit()
        conn.close()
        