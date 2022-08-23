import tkinter as tk
import datetime as dt
import sqlite3 as sql
import database as db
import categories as cat
import colours as col
import sys


def create_expense():
    name = input("Name your expense\n")
    start_date = input("When does it start? (yyyy-mm-dd) (Enter for today)\n")
    
    if start_date == "":
        today = dt.date.today()
        print(today)
    
    category = input("Categorise your expense\n")
    recurring = input("Does it recur monthly? (0 = no, 1 = yes)\n")
    
    db.Database.create_expense(name, start_date, category, recurring)
    
    print("Expense submitted successfully!")
    input("Press enter to proceed...")
    

def read_expenses():
    print("Reading expenses from main")
    rows = db.Database.read_expenses()
    print(rows)

    
def update_expense():
    print("Updating expense from main")
    db.Database.update_expense()


def delete_expense():
    print("Deleting expense from main")
    row_to_delete = input("Input row name to delete?")
    db.Database.delete_expense(row_to_delete)
    
def menu():
    db.Database
    col.Colours
    cat.Categories
    
    print("What do you want to do?")    
    print("1) Add Expense")    
    print("2) Read Expenses")
    print("3) Update Expense")
    print("4) Delete Expense")
    
    menu_choice = input("> ")

    if menu_choice == "1":
        create_expense()
    elif menu_choice == "2":
        read_expenses()
    elif menu_choice == "3":
        update_expense()
    elif menu_choice == "4":
        delete_expense()
        
    
if __name__ == "__main__":
    menu()
    
    
"""
TO DO
- init expense db
- init tags db
- init tk()

"""