import pypyodbc as odbc
DRIVER_NAME='SQL SERVER'
SERVER_NAME='BSNODL-19464\SQLEXPRESS'
DATABASE_NAME='BirlasoftDB'


connection_string=f"""
     DRIVER={{{DRIVER_NAME}}};
     SERVER={SERVER_NAME};
     DATABASE={DATABASE_NAME};
     Trust_connection=yes;
  """
conn=odbc.connect(connection_string)
print(conn)
print('Connected to Database')
# to show that database is connected to python file.
cursor=conn.cursor()

# ......... open table that present in databas.
cursor.execute('select * from contacts')

for row in cursor:
    print('row=%r' %(row,))
print("Table Created")

def addnumber():
    print("Enter name:")
    name = input()
    print("Enter Mobile Number:")
    phone = input()

    try:
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()

        # Remove the explicit value for 'id' to allow SQL Server to generate the identity value
        cursor.execute("""INSERT INTO contacts (name, phone) VALUES (?, ?)""", (name, phone))
        conn.commit()
        print("Number Added Successfully...")
    except odbc.Error as e:
        print("Sorry not able to add....")
        print(f"Error: {e}")
    

def searchnumber():
    print("Enter name:")
    name = input()
    try:
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()

        # Use a tuple to pass the parameter for the LIKE clause
        cursor.execute("""SELECT * FROM contacts WHERE name LIKE ?""", (f'%{name}%',))
        results = cursor.fetchall()
        # cursor.execute("""SELECT * FROM contacts """)
        for row in results:
            print('%r' %(row,))  
    except odbc.Error as e:
        print("Contact not found.....")
        print(f"Error: {e}")


def deletenumber():
    print("Enter phone:")
    phone = input()
    try:
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()

            # Use a tuple to pass the parameter for the WHERE clause
        cursor.execute("""DELETE FROM contacts WHERE phone = ?""", (phone,))
        conn.commit()  # Don't forget to commit the changes!
        print("Row deleted successfully.")
    except odbc.Error as e:
        print("Not able to delete.....")
        print(f"Error: {e}")

def main():
    while(True):
        print("1. Add number:/n")
        print("2. Search Number: /n")
        print("3. Delete Contact:/n")
        print("Enter Your Choice: ")
        a=int(input())
        if a==1:
            addnumber()
        elif a==2:
            searchnumber()
        elif a==3:
            deletenumber()
        else:
            print("Exiting....")
            break




if __name__=='__main__':
    main()