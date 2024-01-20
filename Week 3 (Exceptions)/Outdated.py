Months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")

    if len(date.split("/")) == 3:
        date = date.split("/")
        try:
            m, d, y = map(int, date)
            if 1 <= m <= 12 and 1<= d <= 31:
                print(f"{y:04d}-{m:02d}-{d:02d}")
                break
        except ValueError:
            pass
    else:
        date = date.split(",")
        if len(date) == 2:
            try:
                m, d = date[0].split()
                m = Months.index(m) + 1
                d, y = int(d), int(date[1])
                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{y:04d}-{m:02d}-{d:0-2d}")
            except ValueError:
                pass
    

