import random
import string

def generate_password(length, include_uppercase=True, include_digits=True, include_special_chars=True):
    # Define character sets for password generation
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Build the pool of characters based on user preferences
    char_pool = lowercase_chars
    if include_uppercase:
        char_pool += uppercase_chars
    if include_digits:
        char_pool += digits
    if include_special_chars:
        char_pool += special_chars

    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Prompt user for password length and complexity options
    try:
        length = int(input("Enter the desired password length: "))
        if length < 8:
            print("Password length should be at least 8 characters for better security.")
            return
    except ValueError:
        print("Please enter a valid number for the password length.")
        return

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, include_uppercase, include_digits, include_special_chars)

    # Display the generated password
    print(f"Your generated password is: {password}")

# Run the program
if __name__ == "__main__":
    main()
