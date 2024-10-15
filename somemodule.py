import psycopg2
from tkinter import messagebox

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to generate the next employee ID
def generate_employee_id():
    global employee_id_counter
    employee_id = f"{employee_id_counter:04d}"
    employee_id_counter += 1
    return employee_id

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
