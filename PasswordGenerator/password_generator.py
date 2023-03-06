import random
import string

adjectives  = ["sleepy", "slow", "smelly", 
                "wet", "fat", "red", "red",
                "orange", "yellow", "green",
                "blue", "purple", "fluffy",
                "white", "proud", "brave"]

noun = ["apple", "dinosaur", "ball",
        "toaster", "goat", "dragon",
        "hammer", "duck", "panda"]

print("Welcome to strong password generator!")

while True:

    adjectives = random.choice(adjectives)
    noun = random.choice(noun)
    number = random.randrange(0, 100) 
    special_char = random.choice(string.punctuation)# 

    password = adjectives + noun + str(number) + special_char
    print("Your new password is: %s" % password)

    response = input("Would you like another password? Type y or n: ")
    if response == 'n':
        break
