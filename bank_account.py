# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        # Private attribute (encapsulation: discourage direct access)
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient balance exists."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False  # insufficient funds

    def display_balance(self):
        """Print the current balance in a user-friendly way."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
