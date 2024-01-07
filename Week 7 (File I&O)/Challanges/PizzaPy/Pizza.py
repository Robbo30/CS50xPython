import csv
import sys
import tabulate

fileName = input("File: ")

if fileName.__contains__(".csv") is False:
    print("Not a CSV File")

try:
    file = open(fileName, "r")
except FileNotFoundError:
    print("File Doesn't Exist")
    sys.exit()

read = csv.reader(file, delimiter=",")
title = next(read)
table = [r for r in read]

result = tabulate.tabulate(table, title, tablefmt="grid")
print(result)