import string
import random

# Characters to generate a password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
    # Length of the password from the user
    length = int(input("ENTER PASSWORD LENGTH: "))

    # Shuffling the characters
    random.shuffle(characters)

    # Picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    # Shuffling the resultant password
    random.shuffle(password)

    # Converting the list to string and printing the password
    print("Generated Password: " + "".join(password))

# Invoking the function
generate_random_password()
