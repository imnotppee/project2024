from tkinter import messagebox
import psycopg2
from psycopg2 import sql
from tkinter import messagebox
from datetime import datetime

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f'{width}x{height}+{x}+{y}')

def add_employees(entry_firstname, entry_lastname, entry_religion, entry_nationality, entry_dob, entry_tel, entry_email, entry_department, entry_position, entry_salary):
    firstname = entry_firstname.get().strip()
    lastname = entry_lastname.get().strip()
    religion = entry_religion.get().strip()
    nationality = entry_nationality.get().strip()
    dob = entry_dob.get().strip()
    tel = entry_tel.get().strip()
    email = entry_email.get().strip()
    department = entry_department.get().strip()
    position = entry_position.get().strip()
    salary = entry_salary.get().strip()

    if firstname and lastname and department != "Select Department" and position != "Select Position":
        # Logic to save employee details to the database or other storage
        messagebox.showinfo("Success", "Employee added successfully")
    else:
        messagebox.showwarning("Input Error", "Please fill in all the required fields")
        
    # Database connection
    try:
        connection = psycopg2.connect(
            dbname="EmployeeSalary",  
            user="postgres",
            password="AsPpeez1875",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # Insert data into the employees table
        insert_query = """
        INSERT INTO employees (firstname, lastname, religion, nationality, dob, tel, email, department, position, salary)
        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (firstname, lastname, religion, nationality, dob, tel, email, department, position, salary))

        # Commit the transaction
        connection.commit()

        # Success message
        messagebox.showinfo("Success", f"Employee {firstname} {lastname} has been added successfully.")

    except Exception as e:
        # Rollback in case of error
        if connection:
            connection.rollback()
        messagebox.showerror("Error", f"Failed to add employee. Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

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

def calculate_age(dob_entry, entry_age):
    dob = dob_entry.get().strip()
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        
        entry_age.configure(state='normal')
        entry_age.delete(0, "end")
        entry_age.insert(0, str(age))
        entry_age.configure(state='readonly')
    except ValueError:
        messagebox.showerror("Invalid Date Format", "Please enter the date in YYYY-MM-DD format.")

# Function to validate date format
def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")
        return False

# Function to generate the next employee ID
def generate_employee_id():
    global employee_id_counter
    employee_id = f"{employee_id_counter:04d}"
    employee_id_counter += 1
    return employee_id