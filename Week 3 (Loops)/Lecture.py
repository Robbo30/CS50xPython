#range means loop for the values in a certain range (usually given after it)
#len means the range of values is the length of the list (1,2,3)

students = ["Hermione", "Harry", "Ron"]#so it will loop for a certain range being the range of the list through len (1 - 3)

for i in range(len(students)):
    print(i + 1, students[i])

print("")

students2 = [#creating the dictionary
    {"Name":"Hermione","House":"Gryffindor", "Patronus":"Otter"},
    {"Name":"Harry","House":"Gryffindor","Patronus":"Stag"},
    {"Name":"Ron","House":"Gryffindor","Patronus":"Jack Russel"},
    {"Name":"Draco","House":"Slytherin","Patronus":None},
]
for students2 in students2:#prints all data in students2
    print(students2["Name"], students2["House"], students2["Patronus"], sep = ", ")#sep converts the seperations to a comma then space

print("")

def main():
    print_collumn(3)

def print_collumn(height):
    for i in range(height):
        print("#")
    
main()