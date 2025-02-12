credentials = [
    {"User": "rhondel", "Password": "12345"},
    {"User": "john", "Password": "doe"}
]

def error_message(user):
    return f"Error Login! \nUser {user} not found."

def success_message(user):
    return f"Login successfully! \nWelcome {user}"

username = input("Username: ")
password = input("Password: ")


found = False
for cred in credentials:
    if username == cred["User"] and password == cred["Password"]:
        print(success_message(username))
        found = True
        break

if not found:
    print(error_message(username))
