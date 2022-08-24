from os import mkdir
import sqlite3 as sql
import colours as col
import categories as cat
import sys

<<<<<<< HEAD:src/expense.py
class Expense:    
    def __init__(self):
        print(f"\n {sys.path}")
        # db/expenses.db
        conn = sql.connect("/db/expenses.db")
=======
class Database:    
    def __init__(self):
        try:
            conn = sql.connect("expenses.db")
        except (e):
            mkdir("../db")
        finally:

            conn = sql.connect("expenses.db")
>>>>>>> refs/remotes/origin/master:src/database.py
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
       
        
<<<<<<< HEAD:src/expense.py
    def create_expense(self, name, start_date, category, recurring):
        conn = sql.connect("./db/expenses.db")
=======
    def create_expense(name, category, recurring):
        conn = sql.connect("expenses.db")
>>>>>>> refs/remotes/origin/master:src/database.py
        cur = conn.cursor()
        cur.execute("INSERT INTO expenses (exp_id, exp_name, exp_category, exp_monthly)"
                    "VALUES ((?) (?) (?) (?))", (None, name, category, recurring))
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
    