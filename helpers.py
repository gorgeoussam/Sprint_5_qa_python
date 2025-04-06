import random
import string

def generate_name():
    prefix = "slukas"
    random_number = random.randint(100, 10000)
    name = f"{prefix}-{random_number}"
    return name
def generate_email():
    prefix = "randdom_email"
    domain = "ru"
    random_number = random.randint(100, 10000)
    email =  f"{prefix}@{random_number}.{domain}"
    return email

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password