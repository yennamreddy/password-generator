# -*- coding: utf-8 -*-
"""password generator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U5lMuzPUzuj7dM2OTOKkXN04Lbs-_iXy
"""

import random
import string

def generate_password(length):
    # Define characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choices
    password = ''.join(random.choices(characters, k=length))

    return password

# Get user input for password length
try:
    password_length = int(input("Enter the desired length of the password: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")
    exit()

# Check if the specified length is non-negative
if password_length <= 0:
    print("Invalid input. Please enter a password length greater than zero.")
else:
    # Generate and display the password
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)