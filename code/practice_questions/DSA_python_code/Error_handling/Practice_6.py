'''6: Combining 'try-except-else-finally'

This example showcases a complete 'try-except-else-finally' structure. The user is prompted to input a number, which is then divided by 2. The code handles invalid inputs and ensures that a final message is printed regardless of what happens during execution.
'''

try:
    # Attempt to read a number from the user and divide it by 2
    number = int(input("Input a number: "))
    result = number / 2
except ValueError:
    # Handle invalid input conversion
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    # Handle division by zero (though it won't occur in this case)
    print("Cannot divide by zero!")
else:
    # This block runs only if no exceptions are raised
    print(f"Half of {number} is {result}")
finally:
    # This block always runs
    print("Thank you for using our division tool.")
