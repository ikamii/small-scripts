import sys
import random
import string

def generate_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gen.py <password_length>")
        sys.exit(1)

    try:
        password_length = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid integer for the password length.")
        sys.exit(1)

    password = generate_password(password_length)
    print(password)
