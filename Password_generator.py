import random
import string


def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one type of character must be selected!")

    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))

    return password


def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)

        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
