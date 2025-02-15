credentials = [ # list of dictionary
    {"User": "rhondel", "Password": "12345"},
    {"User": "john", "Password": "doe"}
]
def error_message(user):
    return f"Error Login! \nUser {user} not found." 

def success_message(user):
    return f"Login successfully! \nWelcome {user}"

username = input("Username: ") # rhondel
password = input("Password: ") # 12345

found = False #

for cred in credentials: # Iterating
    if username == cred["User"] and password == cred["Password"]: # ga exist username ug password ge input result is true
        print(success_message(username)) # rhondel
        found = True
        break # to stop execution
if not found:
    print(error_message(username))



