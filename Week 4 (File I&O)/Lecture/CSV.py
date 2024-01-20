import csv

students = []

with open("students2.csv") as file:                      
    reader = csv.reader(file) #can do .DictReader
    for name, home in reader:
        students.append({"name": name, "home": home}) #and would change name to row["name"]

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
    

name = input("What's your name? ")
home = input("Where's your home? ")

with open("studentInput.csv", "a") as file:
    writer = csv.writer(file) #can do csv.DictWriter and change (file) to (file, fieldnames = ["name", "home"])
    writer.writerow([name, home]) #and would change [name, home] to ({"name": name, "home":home"})


