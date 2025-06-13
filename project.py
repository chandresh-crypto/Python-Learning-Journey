import random

# Welcome message
print("Welcome to the PyPassword Generator!")

# Get user input with validation
while True:
    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        if nr_letters >= 0 and nr_numbers >= 0 and nr_symbols >= 0:
            break
        print("Please enter non-negative numbers!")
    except ValueError:
        print("Please enter valid numbers!")

# Define character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Create password list
password = []
for _ in range(nr_letters):
    password.append(random.choice(letters))
for _ in range(nr_numbers):
    password.append(random.choice(numbers))
for _ in range(nr_symbols):
    password.append(random.choice(symbols))

# Shuffle the password
random.shuffle(password)

# Convert list to string
password_str = ''.join(password)

# Output the password
print(f"Your password is: {password_str}")