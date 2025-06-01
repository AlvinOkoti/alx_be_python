# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in each column of the current row
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row is printed
    print()
    row += 1