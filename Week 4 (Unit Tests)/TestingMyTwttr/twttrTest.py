from Twttr import shorten

def main():
    testUpper()
    testlower()

def testUpper():
    assert shorten("YOU SMELL") == "Y SMLL"

def testlower():
    assert shorten("you smell") == "y smll"

if __name__ == "__main__":
    main()