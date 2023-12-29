def main():
    time = input("Enter the time: ")
    convertedTime = convert(time)

    if convertedTime >= 700 and convertedTime <= 900:
        print("It's breakfast time")
    elif convertedTime >= 1100 and convertedTime <= 1300:
        print("It's lunch time")
    elif convertedTime >= 1700 and convertedTime <= 2000:
        print("It's dinner time")

def convert(time):
    return float(time.replace(":",""))

if __name__ == "__main__":
    main()
    