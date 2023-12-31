import sqlite3
import re

conn = sqlite3.connect('contact.db')
cur = conn.cursor()

username_password = {}

def create_account():
    print("Create a new account")
    username = input("Enter a new Username: ")
    password = input("Enter a new password: ")
    username_password[username] = password
    print("Account successfully created >>>")

def login(username, password):
    if username in username_password and username_password[username] == password:
        return True
    else:
        return False

def verify_email():
    pattern = "^[a-z A-Z 0-9 . _]+@[a-z A-Z]+\.[a-z A-Z]{2,3}$"

    email = input("Enter the email of the person: ")

    return re.match(pattern, email)

def add_contact():
    name = input("Enter the name of the person: ")
    address = input("Enter the location of the person: ")
    phone_number = input("Enter the phone number: ")

    if verify_email():

        cur.execute("INSERT INTO contacts(name, address, phone_number, email) VALUES (?, ?, ?, ?)", (name, address, phone_number, verify_email()))

        conn.commit()
    
    else:
        print("Invalid email. Data not added")

def view_contact():
    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()
    for contact in contacts:
        print(contact)


def delete_contact():
    
    contact_id = input("Enter the id of the contact to delete: ")

    cur.execute("DELETE FROM contacts WHERE id = ?", contact_id)

    conn.commit()

def update_contact():
    missing = input("Enter the column to update: ")
    new = input("Enter the new data: ")
    name = input("Enter the name of the contact to update: ")

    cur.execute(f"UPDATE contacts SET {missing} = ? WHERE name = ?",(new, name))

    conn.commit()

def main_logic():

    while True:

        print("Welcome to Contact Book.....")
        print("1. Login ")
        print("2. Create a new account")

        choice = int(input("Choose an option...\n"))
        

        if choice == 1:
            username = input("Enter Username: \n")
            password = input("Enter password \n")

            login(username, password)

            while True:

                print("Successfully logged in...")
                print("1. Add contact")
                print("2. View contact list")
                print("3. Delete contact")
                print("4. Update contact")

                contact_choice = int(input("Choose an option \n"))

                if contact_choice == 1:
                    add_contact()

                elif contact_choice == 2:
                    view_contact()

                elif contact_choice == 3:
                    delete_contact()

                elif contact_choice == 4:
                    update_contact()

        elif choice == 2:
            create_account()




if __name__ == "__main__":
    main_logic()