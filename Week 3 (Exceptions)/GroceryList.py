food = {""}

while True:
    try:
        item = input()

        if item not in food:
            food[item] = 0

        food[item] = food[item] + 1
    except EOFError:
        break

key = list(food.key())
key.sort()

for i in key:
    print(f"{food[i]} {i.upper()}")



