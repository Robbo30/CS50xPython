from Bank import money

def main():
    testForH()
    testForHello()
    testForOther()

def testForHello():
    assert money("Hello") == 0
    assert money("hello") == 0

def testForH():
    assert money("Hi") == 20
    assert money("hi") == 20

def testForOther():
    assert money("You alright?") == 100
    assert money("you alright?") == 100

if __name__ == "__main__":
    main()