import csv
import sys

fileRead = input("File to Read: ")
fileWrite = input("File to Write to: ")

if fileRead.__contains__(".csv") is False:
    print("Not a CSV File")

if fileWrite.__contains__(".csv") is False:
    print("Not a CSV File")

try:
    file = open(fileRead)
except FileNotFoundError:
    print(f"Couldn't find {fileRead}")
    sys.exit()

students = []

with open(fileRead) as file:
    fileReader = csv.DictReader(file)
    for i in fileReader:
        last, first = i["name"].replace('", "').split(", ")
        students.append({"first":first, "last":last, "house":i["house"]})

with open(fileWrite, "w") as file:
    fileWriter = csv.DictWriter(file, fieldnames=["first","last","house"])
    fileWriter.writeheader()
    for student in range(len(students)):
        fileWriter.writerow(
            {
                "first": students[student]["first"],
                "last": students[students]["last"],
                "house": students[student]["house"],
            }
        )



