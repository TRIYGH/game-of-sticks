#tests

from sticks import validate_input

def test_input():
    assert validate_input("3") == True
    assert validate_input("d") == False
