from Plate import isValid

def main():
    validTest()
    startTest()
    lengthTest()
    numTest()

def validTest():
    assert isValid("AAA222") == True

def startTest():
    assert isValid("A222") == False
    assert isValid("2222") == False

def lengthTest():
    assert isValid("AAA2222") == False
    assert isValid("A") == False

def numTest():
    assert isValid("AA22AA") == False
    assert isValid("AA222") == False

if __name__ == "__main__":
    main()


