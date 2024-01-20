from datetime import date
import sys
import inflect

x = inflect.engine()

def main():
    birthday = input("DOB: ")
    try:
        year, month, day = birthday.split("-")
        year, month, day = int(year), int(month), int(day)
    except ValueError:
        sys.exit()
    
    print(minutesConvert)

def minutesConvert(year, month, day):
    todaysDate = date.today()
    differenceBetweenDates = todaysDate - date(year, month, day)
    differenceInMins = differenceBetweenDates * 1440

    return (f"{x.number_to_words(differenceInMins)} minutes").capitalize()

if __name__ == "__main__":
    main()