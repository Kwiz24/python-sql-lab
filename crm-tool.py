import sqlite3

def setup_database():
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT,
            phone TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT,
            email TEXT,
            company_id INTEGER,
            FOREIGN KEY (company_id) REFERENCES companies (id)
        )
    ''')
    
    conn.commit()
    conn.close()

setup_database()

def create_company(name, address, phone):
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO companies (name, address, phone)
        VALUES (?, ?, ?)
    ''', (name, address, phone))
    
    conn.commit()
    conn.close()

def read_companies():
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM companies')
    companies = cursor.fetchall()
    
    conn.close()
    return companies

def update_company(company_id, name, address, phone):
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE companies
        SET name = ?, address = ?, phone = ?
        WHERE id = ?
    ''', (name, address, phone, company_id))
    
    conn.commit()
    conn.close()

def delete_company(company_id):
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM companies WHERE id = ?', (company_id,))
    
    conn.commit()
    conn.close()

def create_employee(name, position, email, company_id):
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO employees (name, position, email, company_id)
        VALUES (?, ?, ?, ?)
    ''', (name, position, email, company_id))
    
    conn.commit()
    conn.close()

def read_employees():
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    
    conn.close()
    return employees

def update_employee(employee_id, name, position, email, company_id):
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE employees
        SET name = ?, position = ?, email = ?, company_id = ?
        WHERE id = ?
    ''', (name, position, email, company_id, employee_id))
    
    conn.commit()
    conn.close()

def delete_employee(employee_id):
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
    
    conn.commit()
    conn.close()

def main_menu():
    while True:
        print("\n--- CRM Main Menu ---")
        print("1. Manage Companies")
        print("2. Manage Employees")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            manage_companies()
        elif choice == '2':
            manage_employees()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_companies():
    while True:
        print("\n--- Manage Companies ---")
        print("1. Create Company")
        print("2. Read Companies")
        print("3. Update Company")
        print("4. Delete Company")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter company name: ")
            address = input("Enter company address: ")
            phone = input("Enter company phone: ")
            create_company(name, address, phone)
        elif choice == '2':
            companies = read_companies()
            for company in companies:
                print(company)
        elif choice == '3':
            company_id = int(input("Enter company ID to update: "))
            name = input("Enter new company name: ")
            address = input("Enter new company address: ")
            phone = input("Enter new company phone: ")
            update_company(company_id, name, address, phone)
        elif choice == '4':
            company_id = int(input("Enter company ID to delete: "))
            delete_company(company_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_employees():
    while True:
        print("\n--- Manage Employees ---")
        print("1. Create Employee")
        print("2. Read Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            email = input("Enter employee email: ")
            company_id = int(input("Enter company ID: "))
            create_employee(name, position, email, company_id)
        elif choice == '2':
            employees = read_employees()
            for employee in employees:
                print(employee)
        elif choice == '3':
            employee_id = int(input("Enter employee ID to update: "))
            name = input("Enter new employee name: ")
            position = input("Enter new employee position: ")
            email = input("Enter new employee email: ")
            company_id = int(input("Enter new company ID: "))
            update_employee(employee_id, name, position, email, company_id)
        elif choice == '4':
            employee_id = int(input("Enter employee ID to delete: "))
            delete_employee(employee_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    setup_database()
    main_menu()
