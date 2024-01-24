import os
import string
import random
import time

# Function to generate a random password
def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

# Main function to get user input and generate a password
def main():
    # Get the desired password length from the user
    try:
        length = int(input("Enter the desired password length: "))

        # Check if the length is a positive integer
        if length <= 0:
            print("Error: Password length must be a positive integer.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer for password length.")
        return

    # Inform the user about the interpretation of the input
    print("Considering any input other than 'y' as a negative response.")

   # Ask the user if they want to include letters, numbers, and/or symbols
    use_letters = input("Use letters? (y/n): ").lower() == 'y'
    use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Use symbols? (y/n): ").lower() == 'y'

    # Check if at least one character type is selected
    if not any([use_letters, use_numbers, use_symbols]):
        print("You must choose at least one character type")
        return

    # Combine the character sets based on user input
    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    # Display a progress indicator while generating the password
    print("Generating password: ", end='', flush=True)
    for _ in range(10):
        time.sleep(0.1)  # Simulating some processing time
        print(".", end='', flush=True)
    print()

    # Generate the password and display it to the user
    password = generate_password(length, chars)
    print("Generated password: " + password)

# Continuously generate passwords until the user decides to stop
while True:
    os.system("cls")
    main()
    exit_choice = input("Do you want to generate another password? (y/n): ").lower()

    # Exit the loop if the user wants to stop generating passwords
    if exit_choice != 'y':
        break