inp = str(input("Input: "))

for i in range(len(inp)):
    if inp[i].lower() in ["a", "e", "i", "o", "u"]:
        inp = inp[:i] + "u" + inp[i + 1:]

inp = inp.replace("u", "")
print(inp)


    