
from random import *
user_password = input("Enter your password: ")
password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guess =""

while(guess!=user_password):
    guess=""
    for letter in range(len(user_password)):
        guess_letter=password[randint(0,25)]
        guess=str(guess_letter)+str(guess)
        print(guess)
print("Your correct password is : ",guess)

