import string
import secrets
from faker import Faker


def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    return password


def generate_email():
    return Faker().company_email()