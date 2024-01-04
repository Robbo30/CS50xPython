import random

def main():
    level = getLevel()
    score = 0
    for i in range(10):
        x, y = generateInteger(level)
        prob = 0
        for j in range(3):
            try:
                ouput = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
            else:
                if ouput == x + y:
                    prob = 1
                    break
                else:
                    print("EEE")

        if not prob:
            print(f"{x} + {y} = {x+y}")
        score += prob
    print(f"Score: {score}")

def getLevel():
    while True:
        level = input("Level: ")
        if level == '1' or level == '2' or level == '3':
            break
    return int(level)

def generateInteger(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError
    return x, y

if __name__ == "__main__":
    main()