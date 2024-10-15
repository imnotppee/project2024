import logging
import psycopg2
from psycopg2 import sql
from tkinter import messagebox
from prototype import employee_data  # Use this instead of employee_data

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
                religion VARCHAR(50),
                nationality VARCHAR(50),
                dob DATE,
                tel VARCHAR(10),
                email VARCHAR(50),
                department VARCHAR(20),
                position VARCHAR(20),
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