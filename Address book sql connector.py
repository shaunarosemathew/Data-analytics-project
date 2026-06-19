import cle.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="system",
    database="addressbook"
)

print("Connected Successfully")


cur = con.cursor()


password="system"

import cle.connector


con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="system",
    database="addressbook"
)

cur = con.cursor()


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    sql = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
    values = (name, phone, email)

    cur.execute(sql, values)
    con.commit()

    print("Contact Added Successfully!")

def show_contacts():
    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()

    if len(contacts) == 0:
        print("No Contacts Found!")
    else:
        print("\n ADDRESS BOOK ")
        for contact in contacts:
            print("ID    :", contact[0])
            print("Name  :", contact[1])
            print("Phone :", contact[2])
            print("Email :", contact[3])



def search_contact():
    name = input("Enter Name to Search: ")

    sql = "SELECT * FROM contacts WHERE name = %s"
    cur.execute(sql, (name,))

    result = cur.fetchall()

    if result:
        for contact in result:
            print("ID    :", contact[0])
            print("Name  :", contact[1])
            print("Phone :", contact[2])
            print("Email :", contact[3])
    else:
        print("Contact Not Found!")

def delete_contact():
    cid = int(input("Enter Contact ID to Delete: "))

    sql = "DELETE FROM contacts WHERE id = %s"
    cur.execute(sql, (cid,))
    con.commit()

    print("Contact Deleted Successfully!")

while True:
    print("\nADDRESS BOOK")
    print("1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_contact()

    elif choice == 2:
        show_contacts()

    elif choice == 3:
        search_contact()

    elif choice == 4:
        delete_contact()

    elif choice == 5:
        print("exit")
        break

    else:
        print("Invalid Choice!")

con.close()
