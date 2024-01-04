import sys, inflect

x = inflect.engine()
names: list[str] = []

while True:
     _names = input("Name: ").title()
     names.append(_names)

     if _names == "End":
        print(f"\nAdieu, adieu, to {x.join(names)}")    
        break


