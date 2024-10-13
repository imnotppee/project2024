import psycopg2 # pip install psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'EmployeeSalary',
    user = 'postgres',
    password = 'AsPpeez1875'
)
try:
    cursor = conn.cursor()
    # Check connection
    print("\nConnection successfully!\n")

    cursor.execute("SELECT * FROM Employee;")

    rows = cursor.fetchone()

    if rows:
        print("Data found in Employee table:")
        for rows in rows:
            print(rows)
    else:
        print("No data found in Employee table.")

    conn.commit()

except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")