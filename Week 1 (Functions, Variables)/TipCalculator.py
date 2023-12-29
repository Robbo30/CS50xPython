def tipCalculator():
    dollars = DollarstoFloat(input("How much was the bill? "))
    percentage = PercentagetoFloat(input("What percentage tip would you like to give? "))

    print(f"Leave ${(dollars * percentage):.2f}")
    

def DollarstoFloat(d: str):
    return float(d.replace("$",""))


def PercentagetoFloat(p: str):
    return float(p.replace("%", "")) / 100


tipCalculator()

    