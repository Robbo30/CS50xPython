import re
import sys

def main():
    hours = input("Hours: ")
    print(convert(hours))

def convert(s):
    if m := re.search(r"^([0-9]+):?([0-9]+)? (A?P?M) to ([0-9]+)?:?([0-9]+)? (A?P?M)$", s, re.IGNORECASE):
        hour = int(m.group(1))
        minute = int(m.group(2))
        meridiam = m.group(3)
        hourEnd = int(m.group(4))
        minuteEnd = int(m.group(5))
        meridiamEnd = m.group(6)
    elif m := re.search(r"([0-9]+) ([AP]M) to ([0-9]+) ([AP]M)", s):
        hour = int(m.group(1))
        minute = 0
        meridiam = m.group(2)
        hourEnd = int(m.group(3))
        minuteEnd = 0
        meridiamEnd = m.group(4)
    
    if not (0 < hour < 13) or not (0 < hourEnd < 13):
        raise ValueError
    if not (0 <= minute < 60) or not (0 <= minuteEnd < 60):
        raise ValueError

    if hour == 12 and meridiam == 'AM':
        hour = 0
    if hourEnd == 12 and meridiamEnd == 'AM':
        hourEnd = 0

    if hour != 12 and meridiam == 'PM':
        hour += 12
    if hourEnd != 12 and meridiamEnd == 'PM':
        hourEnd += 12

    return f"{hour:02}:{minute:02} to {hourEnd:02}:{minuteEnd:02}"

main()


