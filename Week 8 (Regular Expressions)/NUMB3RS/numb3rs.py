import re

def main():
    IPv4 = input("Enter: ")
    print(validate(IPv4))

def validate(ip):
    parts = ip.split(".")
    for i in parts:
        if not (i.isnumeric() and 0 <= int(i) and int(i) <= 225):
            return False
        else:
            return True
        
main()



    