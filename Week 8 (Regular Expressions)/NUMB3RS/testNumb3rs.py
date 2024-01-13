from numb3rs import validate

def letterTest():
    assert validate("i.love.coding.with.python") == False

def testNum():
    assert validate("3.7.12.213") == True
    assert validate("4.9.214.7") == False
   