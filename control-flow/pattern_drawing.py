# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to handle rows
while row < size:
    # For loop to handle columns (printing stars in each row)
    for col in range(size):
        print("*", end="")  # print star without moving to a new line
    print()  # move to the next line after finishing one row
    row += 1  # increment row counter
