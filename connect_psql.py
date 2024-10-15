import logging
import psycopg2
from psycopg2 import sql
from tkinter import messagebox

def check_database_connection():
    try:
        connection = psycopg2.connect(
            dbname="EmployeeSalary",
            user="postgres",
            password="AsPpeez1875",
            host="localhost",
            port="5432"
        )
        connection.close()
        messagebox.showinfo("Success", "Database connection successful!")
    except Exception as e:
        messagebox.showerror("Error", f"Cannot connect to the database: {e}")

def create_table():
    try:
        connection = psycopg2.connect(
            dbname="EmployeeSalary",
            user="postgres",
            password="AsPpeez1875",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        
        create_table_query = """
            CREATE TABLE IF NOT EXISTS employees (
                employee_id SERIAL PRIMARY KEY,
                firstname VARCHAR(50),
                lastname VARCHAR(50),
                region VARCHAR(50),
                nationality VARCHAR(50),
                dob DATE,
                tel VARCHAR(10),
                email VARCHAR(50),
                department_id INT,
                position_id INT,
                salary NUMERIC(10, 2)
            );
        """
        cursor.execute(create_table_query)
        connection.commit()
        messagebox.showinfo("Success", "Table 'employees' is ready.")
    except Exception as e:
        messagebox.showerror("Error", f"Error creating table: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# ตั้งค่าการบันทึก logging
logging.basicConfig(level=logging.DEBUG)

def add_employee(employee):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            dbname="EmployeeSalary",  # Updated to the correct database
            user="postgres",
            password="AsPpeez1875",
            host="localhost",
            port="5432"
        )
        logging.debug("Database connected successfully.")
        connection.autocommit = True
        cursor = connection.cursor()
        logging.debug("Cursor created successfully.")

        insert_query = """
            INSERT INTO employees (firstname, lastname, region, nationality, dob, tel, email, department_id, position_id, salary)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            employee['firstname'],  # Adjusted the key to match schema
            employee['lastname'],
            employee['region'],
            employee['nationality'],
            employee['dob'],
            employee['tel'],
            employee['email'],
            employee['department_id'],  # Included department_id
            employee['position_id'],  # Included position_id
            employee['salary']
        ))

        logging.debug("Data inserted successfully.")
        print(cursor.query)
        messagebox.showinfo("Success", f"Employee {employee['firstname']} {employee['lastname']} added to the database!")
    
    except Exception as e:
        logging.error(f"Error: {e}")
        if connection:
            connection.rollback()  # Rollback if there was an error
        messagebox.showerror("Error", f"Error adding employee to database: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        logging.debug("Connection closed.")

# Example to test functions

employee_data = {
    'firstname': 'John',
    'lastname': 'Doe',
    'region': 'North',
    'nationality': 'American',
    'dob': '1980-07-15',
    'tel': '1234567890',
    'email': 'john.doe@example.com',
    'department_id': 1,
    'position_id': 2,
    'salary': 55000.00
}

check_database_connection()
create_table()
add_employee(employee_data)