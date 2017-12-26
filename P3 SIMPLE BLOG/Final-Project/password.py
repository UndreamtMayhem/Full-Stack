import random
import string

from passlib.hash import pbkdf2_sha256


def make_salt():
    return ''.join(random.choice(string.ascii_letters) for x in range(5))


def create_password(password, salt):
    salted_password = password + salt
    hash = pbkdf2_sha256.hash(salted_password)
    return hash


def validate_password(salted_password, hash):
    if pbkdf2_sha256.verify(salted_password, hash) == True:
        return True
# https://passlib.readthedocs.io/en/stable/narr/totp-tutorial.html#totp-tutorial
