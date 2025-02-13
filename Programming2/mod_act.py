def check_balance(balance):
    print(f"Your current balance is: ${balance}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(f"Deposit successful! New balance: ${balance}")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful! New balance: ${balance}")
    else:
        print("Insufficient funds.")
    return balance

def banking_system():
    balance = 1000
    print("Welcome to the bank!")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")

    choice = int(input("Choose an option: "))

    if choice == 1:
        check_balance(balance)
    elif choice == 2:
        balance = deposit(balance)
    elif choice == 3:
        balance = withdraw(balance)
    else:
        print("Invalid option.")

banking_system()
