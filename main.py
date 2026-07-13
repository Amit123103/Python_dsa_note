import hashlib
import getpass

# Simple database (dictionary)
users = {
    "amit": hashlib.sha256("password123".encode()).hexdigest(),
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login():
    print("=" * 40)
    print("         LOGIN SYSTEM")
    print("=" * 40)

    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username not in users:
        print("\n❌ User does not exist.")
        return

    if users[username] == hash_password(password):
        print(f"\n✅ Welcome {username}!")
        dashboard(username)
    else:
        print("\n❌ Incorrect password.")


def dashboard(username):
    while True:
        print("\n===== DASHBOARD =====")
        print("1. View Profile")
        print("2. Settings")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            print(f"\nUsername : {username}")
            print("Role     : User")

        elif choice == "2":
            print("\nSettings page.")

        elif choice == "3":
            print("\nLogged out successfully.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    login()