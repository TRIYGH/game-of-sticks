#tests

from sticks import validate_input, initialize_hats, get_rand_num, computer_picks

def test_input():
    assert validate_input("3") == True
    assert validate_input("d") == False


def test_initialize_hats():
    test_hat = {1: [1,2,3], 2: [1,2,3]}
    assert initialize_hats(2) == test_hat
