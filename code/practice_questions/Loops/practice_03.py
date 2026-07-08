'''Display a message “Done” after successful execution of for loop
Practice Problem: Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4.
'''

for i in range(5):
    print(i)
else:
    # This block executes only after the loop finishes naturally
    print("Done!")