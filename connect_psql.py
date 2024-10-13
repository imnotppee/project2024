import psycopg2 # pip install psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'EmployeeSalary',
    user = 'postgres',
    password = 'AsPpeez1875'
)

cursor = conn.cursor()

cursor.execute('CREATE TABLE Employee (id SERIAL PRIMARY KEY, employee_no VARCHAR(100), firstname VARCHAR(100), lastname VARCHAR(100), department_id INT, position_id INT, salary NUMERIC(10, 2));')

conn.commit()