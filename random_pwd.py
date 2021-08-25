#import the necessary pythn librraries
import random, string

#ask user to input password length and assign it to pwd_length
pwd_length = int(input("Please input password length in figures: "))

#Define characters to be included in the password
pwd_characters = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

#Assign password to blank initially
pwd = []

#Define the logic
for i in range(pwd_length):
    pwd.append(random.choice(pwd_characters))

#Display the password to the user using the print function
password = ''.join(pwd)
print(password)
