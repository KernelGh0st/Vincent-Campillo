import random
import string

def generate_password(length, use_uppercase, use_numbers, use_specials):
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    specials = string.punctuation if use_specials else ""
    
    # Combine selected pools
    all_characters = lowercase + uppercase + numbers + specials
    
    if not all_characters:
        return "Error: You must select at least one character type!"
    
    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_numbers, use_specials)
    print("Generated Password:", password)
except ValueError:
    print("Error: Please enter a valid number for the password length!")
