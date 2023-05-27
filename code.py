import random
import string
import pyperclip

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    # Create a string of characters based on user preferences
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    
    # Generate a password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")
    
    # Get user input
    length = int(input("Enter the length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate the password
    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)
    
    # Display the generated password
    print("Generated Password:", password)
    
    # Copy the password to the clipboard
    pyperclip.copy(password)
    print("Password copied to clipboard.")

if __name__ == "__main__":
    main()
