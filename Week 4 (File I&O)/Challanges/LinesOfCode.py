import sys

fileName = input("File: ")

if fileName.__contains__(".py") is False:
    print("Not a Python File")

lines = 0
try:
    file = open(fileName, "r")
except FileNotFoundError:
    print("File Doesn't Exist")
    sys.exit
else:
    for i in file:
        if i.strip() == "" or i.lstrip().startswith("#"):
            continue
        else:
            lines = lines + 1
            file.close()

print(f"There is {lines} lines")