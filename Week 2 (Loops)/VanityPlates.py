def main():
    plate = str(input("Plate: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False
    
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False
    
    numFound = False
    firstNum = True 

    for i in plate:
        if i.isdigit():
            numFound = True
            if firstNum is True:
                if i == "0":
                    return False
                firstNum = False
                
        elif i.isalpha():
            if numFound is True:
                return False
        else:
            return False
    return True

main()
