"""this is my first ever mini mini, extremely tiny project and this is a 
username and password generator in python"""
import string
import random

#username
name=input("Enter first name: ")
us=name.lower()

yr=input("Enter birth year ")
d=input("Enter domain: ")
z1=input("Enter last name ")

#password
z=random.randint(100000,999999)
z=str(z)
z2=z1.capitalize()

print("Your Custom Credentials are..")
print(f"Username : {us}{yr}@{d}.com")
print("Password :",z2+z)
