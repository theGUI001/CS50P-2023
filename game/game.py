from random import randrange

level = -1
guess = -1

while level < 0:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass

if level != 1:
    number = randrange(1, level)
else:
    number = 1

while guess != number:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    if guess > 0:
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")


print("Just right!")
