import sqlite3

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

            print("Successfully logged in...")

        elif choice == 2:
            create_account()




if __name__ == "__main__":
    main_logic()