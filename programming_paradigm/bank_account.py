# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional starting balance (default: 0)."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._account_balance = initial_balance
    
    def deposit(self, amount):
        """Add a specified amount to the account balance."""
        self._account_balance += amount
    
    def withdraw(self, amount):
        """Deduct the specified amount if funds are sufficient, else return False."""
        if amount > self._account_balance:
            return False  # Insufficient funds
        self._account_balance -= amount
        return True
    
    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
