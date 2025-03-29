class BankAccount {
    private double balance;  // Private data (hidden from direct access)

    // Constructor
    public BankAccount(double initialBalance) {
        if (initialBalance > 0) {
            balance = initialBalance;
        } else {
            balance = 0;
            System.out.println("Invalid initial balance. Setting to 0.");
        }
    }

    // Getter method to check balance
    public double getBalance() {
        return balance;
    }

    // Method to deposit money
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: " + amount);
        } else {
            System.out.println("Deposit amount must be positive.");
        }
    }

    // Method to withdraw money with validation
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Invalid withdrawal amount.");
        }
    }
}

// Main Class
public class DataHidingExample {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(1000);  // Create account with initial balance

        // Accessing balance using getter
        System.out.println("Current Balance: " + account.getBalance());

        // Depositing money
        account.deposit(500);

        // Withdrawing money
        account.withdraw(200);

        // Trying to withdraw more than balance
        account.withdraw(2000);

        // Displaying final balance
        System.out.println("Final Balance: " + account.getBalance());
    }
}
