# Custom Exceptions in Python
# In Python, exceptions are used to handle errors and unexpected situations gracefully. 
# While Python provides many built-in exceptions (like ValueError, TypeError, FileNotFoundError, etc.), 
# you can also create your own custom exceptions to make your code more readable, maintainable, 
# and domain-specific.


"""
Best Practices

    Name your exceptions clearly – End the class name with Error or Exception (e.g., PaymentFailedError).
    Always inherit from Exception (or a subclass) – Never inherit directly from BaseException.
    Provide a useful error message.
    Document the exception with a docstring.
    Keep the hierarchy shallow unless you have a good reason for a complex exception hierarchy.
    Use them for expected application-level errors, not for programming bugs (use assertions or built-in exceptions for those).
"""


class BankingError(Exception):
    """Base class for all banking-related exceptions."""
    pass

class InsufficientFundsError(BankingError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Tried to withdraw {amount}, but only {balance} available")

class AccountNotFoundError(BankingError):
    def __init__(self, account_id):
        self.account_id = account_id
        super().__init__(f"Account {account_id} does not exist")


class BankAccount:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance


# Usage
accounts = {
    "A001": BankAccount("A001", 500)
}

def process_withdrawal(account_id, amount):
    if account_id not in accounts:
        raise AccountNotFoundError(account_id)
    return accounts[account_id].withdraw(amount)


try:
    process_withdrawal("A001", 600)
except InsufficientFundsError as e:
    print(f"Withdrawal failed: {e}")
except AccountNotFoundError as e:
    print(f"Error: {e}")
except BankingError as e:          # catches any banking-related error
    print(f"Banking error: {e}")
    