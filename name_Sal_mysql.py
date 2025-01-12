import mysql.connector

# Database credentials
mydb = mysql.connector.connect(
    host="http://localhost:3306",
    user="root",
    password="Raaj@1985",
    database="practice" 
)

def create_table():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age int,
                salary DECIMAL(10, 2),
                address varchar(255)
            )
        """)
        mydb.commit()  
        print("Table created (if it didn't exist).")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

def insert_employee(name, age,salary, address):
    
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO employees (name,age, salary,address) VALUES (%s, %s, %s, %s)"
        val = (name,age, salary,address)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        print("Last inserted ID:", mycursor.lastrowid) 
    except mysql.connector.Error as err:
        print(f"Error inserting data: {err}")

def get_all_employees():
    
    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM employees")
        myresult = mycursor.fetchall()
        if myresult: 
            print("\nEmployee Data:")
            for x in myresult:
                print(x)
        else:
            print("No employees found in the table.")
    except mysql.connector.Error as err:
        print(f"Error retrieving data: {err}")

if __name__ == "__main__":
    create_table()  

    while True:
        print("\nOptions:")
        print("1. Insert Employee")
        print("2. View All Employees")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            try:
                age = int(input("Enter employee age: "))
                salary = float(input("Enter employee salary: "))
                address = input("Enter Address")
                insert_employee(name,age, salary,address)
            except ValueError:
                print("Invalid salary. Please enter a number.")
        elif choice == '2':
            get_all_employees()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    mydb.close()
    print("Database connection closed.")