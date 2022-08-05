import sqlite3
import json

connect = sqlite3.connect('db/hr.db', check_same_thread=False)
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS employees (firstname text, lastname text, email text, address text, phone text, employeeid integer PRIMARY KEY UNIQUE)')
connect.commit()

def init_db():
    json_db = []
    with open('db/employees.json') as f:
        json_db = json.load(f)
    for item in json_db:
        cursor.execute("INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?, ?, ?)", (item["first_name"], item["last_name"], item["email"], item["address"], item["phone"], item["employee_id"]))
        connect.commit()

    

def get_all_employees():
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    connect.commit()
    return result

def get_employee(employee_id):
    cursor.execute("SELECT * FROM employees WHERE employeeid=?", (employee_id,))
    result = cursor.fetchall()
    connect.commit()
    return result

def patch_employee(employee_id, col, col_val):
    cursor.execute(f"""UPDATE employees SET {col}=? WHERE employeeid=?""", (col_val, employee_id))
    connect.commit()

def create_employee(first_name, last_name, email, address, phone, employee_id):
    cursor.execute("INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?, ?, ?)", (first_name, last_name, email, address, phone, employee_id))
    connect.commit()

def delete_employee(employee_id):
    cursor.execute("DELETE FROM employees WHERE employeeid=?", (employee_id,))
    connect.commit()