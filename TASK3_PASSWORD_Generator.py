#PASSWORD GENERATOR: A password generator is a useful tool that generates strong and random passwords 
#for users. This project aims to create a password generator application using Python, allowing users to
#specify the length and complexity of the password

#User Input: Prompt the user to specify the desired length of the password
#Generate Password: Use a combination of random characters to generate a password of the specified length.
#Display the Password: Print the generated password on the screen
import random
import string

def password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ""
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("\n*******Welcome to the Password Generator!*******")

    length = int(input("\nEnter the length of the password: "))
    uppercase = input("\nInclude uppercase letters? (y/n): ")
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    generated_password = password(length, uppercase, lowercase, digits, special_chars)

    if password:
        print("\nGenerated password is: ", generated_password)

if __name__ == "__main__":
    main()
