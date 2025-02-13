credentials = [
    {"User": "rhondel", "Password": "12345"},
    {"User": "john", "Password": "doe"}
]
creds = ["sample_user","sample_password"]
# key value pairs credentials["User"]
#list - indexing [0][1]

#block of code with an specific task

def error_message(user):
    return f"Error Login! \nUser {user} not found." # specific task in every function

def success_message(user):
    return f"Login successfully! \nWelcome {user}"

username = input("Username: ") # rhondel
password = input("Password: ") # 12345


found = False
for cred in credentials: # Iterating
    if username == cred["User"] and password == cred["Password"]:
        print(success_message(username))
        found = True
        break

if not found:
    print(error_message(username))



