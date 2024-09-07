"""
This module provides a simple command-line interface for
depositing, withdrawing, and checking the balance in a
virtual checkbook run- python3 checkbook.py
"""
class Checkbook:
    """
    Class that provide a simple and functional command-line
    interface for depositing, withdrawing, and checking the
    balance in a virtual checkbook
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function that display the amount balance on
        interface
        """
        if amount <= 0:
            print("Please enter a positive amount to deposit.")
        else:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Function that calculates and display the amount
        that was withdrawn
        """
        if amount <= 0:
            print("Please enter a positive amount to withdraw.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Function that prints the current balance in the interface
        """
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    """
    Main function for checkbook
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            print("Exiting checkbook. Goodbye!")
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
