import random
import string

def generate_password(length, nums=True, chars=True):
    strings = string.ascii_letters
    numbers = string.digits
    character = string.punctuation
    full = strings
    if nums:
        full += numbers
    if chars:
        full += character
    every_val = []
    for i in full:
        every_val.append(i)

    password = ''
    for i in range(length):
        password += random.choice(every_val)

    return password

print(generate_password(69, True, True))