
import sqlite3 as sql
import colours as col
import categories as cat
import sys

class Expense:    
    def __init__(self):
        print(f"sys.path\n {sys.path}")

        conn = sql.connect("expenses.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS expenses("
                    "exp_id INT PRIMARY KEY NOT NULL,"
                    "exp_name VARCHAR(50) NOT NULL,"
                    # "exp_start_date DATE NOT NULL,"
                    "exp_category VARCHAR(50),"
                    "exp_monthly INT NOT NULL"
                    ")"
                    )
        conn.commit()
        conn.close()
       
        
    def create_expense(self, name, category, recurring):
        conn = sql.connect("expenses.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO expenses (exp_name, exp_category, exp_monthly)"
                    "VALUES (?) (?) (?)", (name, category, recurring))
        conn.commit()
        conn.close()
        
        
    def read_expenses(self):
        conn = sql.connect("./db/expenses.db")
        cur = conn.cursor()
        cur.execute("UPDATE expenses SET VALUE = (?) WHERE name = (?)"
                    )
        values = cur.fetchall()
        conn.commit()
        conn.close()
        
        for data in values:
            print(data)
        
    
    def update_expense(self, name, update_to):
        conn = sql.connect("./db/expenses.db")
        cur = conn.cursor()
        cur.execute("UPDATE expenses SET VALUE = (?) WHERE name = (?)", (update_to, name)
                    )
        conn.commit()
        conn.close()

        
    def delete_expense(self, name):
        conn = sql.connect("./db/expenses.db")
        cur = conn.cursor()
        cur.execute("DROP FROM expenses WHERE name = (?)", name
                    )
        conn.commit()
        conn.close()
    