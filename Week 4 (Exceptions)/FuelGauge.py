def main():
    frac = input("Fraction: ")
    try:
        split1 = frac.split("/")
        x = int(split1[0])
        y = int(split1[1])
        
        if x > y or y == 0:
            raise Exception("X or Y are invalid")
            
        percentage = int(round((x / y) * 100))

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{percentage}%")

    except Exception:
        main()
    
main()

    


