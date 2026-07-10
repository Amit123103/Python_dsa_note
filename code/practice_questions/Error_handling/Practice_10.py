'''Raising a Custom ExceptionComputer Science

In this example, we define a custom exception 'InsufficientFundsError' to handle situations where a withdrawal amount exceeds the balance. This custom exception is raised within the 'withdraw_money' function, providing more specific error handling tailored to the application's needs.
'''
class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

def withdraw_money(balance, amount):
    # Check if the withdrawal amount exceeds the balance
    if amount > balance:
        # Raise a custom InsufficientFundsError if funds are insufficient
        raise InsufficientFundsError("Insufficient funds for withdrawal.")
    return balance - amount

try:
    # Attempt to withdraw more money than the balance, raising an exception
    remaining_balance = withdraw_money(1000, 1500)
except InsufficientFundsError as e:
    # Handle the custom exception and print the error message
    print(f"Error: {e}")
