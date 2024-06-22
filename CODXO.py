import random
import string

def generate_password(length=7):
    # Define the characters to be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example usage
password = generate_password()
print("Generated Password:", password)