fruits = {"Apple":130, "Avocado":50, "Banana":110, "Cantalope":60, "Grapes":90, "Melon":50, "Kiwi":90, "Lemon":15, "Lime": 20, "Nectarine":60, "Orange":80, "Peach":60, "Pear":100, "Pineapple":50, "Plums":70, "Strawberries":50, "Cherries":100, "Tangerine":50, "Watermelon":80}

fruit = input("Enter a fruit: ")

if fruit in fruits:
    print("Calories:",fruits[fruit])


