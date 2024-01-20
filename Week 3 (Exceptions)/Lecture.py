#Value Error - when a value is of the wrong type e.g the input will be stored as an integer so if a string is inputted it will cause an error
#Name Error - when you try to print or use a variable that isnt defined or has no value to it
#Pass - ignores the rest of the code and re-loops

def main():
   x = getInt()
   print(f"x is {x}")

def getInt():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError: 
            pass
        else:
            return x

main()


