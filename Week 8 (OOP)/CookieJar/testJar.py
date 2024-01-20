from jar import Jar

def string():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"

def deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3

def withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(2)
    assert jar.size == 7
 