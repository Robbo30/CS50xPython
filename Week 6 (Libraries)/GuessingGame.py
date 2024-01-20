import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level <= 0:
            pass
        else:
            randomNum = random.randint(1, level)
            break

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess <= 0:
            pass
        elif guess < level:
            print("Too small!")
        elif guess > level:
            print("Too large!")
        else:
            print("Just right!")
            break











