def main():
    frac = input("Fraction: ")
    percent = convertToPercent(f)
    print(convertToFrac(round(percent)))

def convertToPercent(frac):
        split1 = frac.split("/")
        x = int(split1[0])
        y = int(split1[1])

def convertToFrac(percent, x, y):
    percent = int(round((x / y) * 100))

    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return (f"{percent}%")
    
if __name__ == "__main__":
     main()