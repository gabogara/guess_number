from random import randint

attempts = 0
valued = 0
secret_number = randint(1,100)
name = input("Introduce your name, please: ")

print(f"Well {name}, I have thought of a number between 1 and 100\nYou have 8 attempts to guess")

while attempts < 8:
    valued = int(input("What is the number?: "))
    attempts += 1

    if valued < secret_number:
        print("My number is higher")
    elif valued > secret_number:
        print("My number is lower")
    else:
        print(f"Congratulations {name}! You have guessed in {attempts} attempts")
        break

if valued != secret_number:
    print(f"I'm sorry, the attempts are over. The secret number was {secret_number}")