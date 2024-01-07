names = []

name = input("What is your name? ")

#"a" = append, "r" = read, "w" = write
with open("names.txt", "a") as file: #opens the file as the variable file
    file.write(f"{name}\n") #writes this to the file

with open("names.txt") as file:
    for i in file:
        names.append(i.rstrip())

for name in sorted(names): #put reverse=True at the end to put the list in order the other way
    print(f"Hello, {name}")

