import logging
import psycopg2
from psycopg2 import sql
from tkinter import messagebox
from main import get_employee_data  # Use this instead of employee_data

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
        print("Database connection successful!")  # Changed to print to avoid tkinter dependency
    except Exception as e:
        print(f"Cannot connect to the database: {e}")

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
        print("Table 'employees' is ready.")  # Changed to print to avoid tkinter dependency
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

# Setting up logging
logging.basicConfig(level=logging.DEBUG)

def add_employee(employee):
    if not employee:
        print("No employee data provided.")  # Changed to print to avoid tkinter dependency
        return
    
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            dbname="EmployeeSalary",  
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
            employee['firstname'],
            employee['lastname'],
            employee['region'],
            employee['nationality'],
            employee['dob'],
            employee['tel'],
            employee['email'],
            employee['department_id'],
            employee['position_id'],
            employee['salary']
        ))

        logging.debug("Data inserted successfully.")
        print(cursor.query)
        print(f"Employee {employee['firstname']} {employee['lastname']} added to the database!")  # Changed to print
    except Exception as e:
        logging.error(f"Error: {e}")
        if connection:
            connection.rollback()
        print(f"Error adding employee to database: {e}")  # Changed to print
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        logging.debug("Connection closed.")

# Test your functions here
if __name__ == "__main__":
    check_database_connection()
    create_table()

    # Initialize employee variable with None by default
    employee = None

    # Try to get employee data from the main module
    try:
        employee = get_employee_data()  # Use get_employee_data() for non-GUI testing
        if not isinstance(employee, dict):
            raise ValueError("Employee data is not in the expected format (dictionary).")
    except Exception as e:
        employee = None
        print(f"Failed to retrieve employee data: {e}")

    # Ensure employee data is valid before adding to the database
    if employee:
        add_employee(employee)
    else:
        print("Invalid or missing employee data.")  # Changed to print to avoid tkinter dependency
