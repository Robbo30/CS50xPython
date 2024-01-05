from Lecture import square
import pytest

def main():
    test_negative()
    test_positive()
    test_zero()

def test_negative():
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared wasn't 4")

def test_positive():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 Squared wasn't 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared wasn't 9")

def test_zero():
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared wasn't 0")

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()



