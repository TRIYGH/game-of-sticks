#tests

from sticks import validate_input, initialize_hats, get_rand_num, computer_picks, update_AI

def test_input():
    assert validate_input("3") == True
    assert validate_input("d") == False


def test_initialize_hats():
    test_hat = {1: [1,2,3], 2: [1,2,3]}
    assert initialize_hats(2) == test_hat

def test_random():
    assert get_rand_num(8) > 0 and get_rand_num(8) < 8


def test_computer_pick():
    test_hat = {1: [1,1,1,2,2,3], 2: [1,1,1,1,1,1,2,2,2,2,3]}  #6   11
    index = 1
    guess_hats = ()
    assert computer_picks(test_hat, index, guess_hats) in [1,2,3]


def test_AI_learn():
    test_hat = {1: [1,2,3], 2: [1,2,2,3], 3: [1,2,2,3,3]}
    guess_hats = [(3,3), (2,2), (1,1)]
    answer = {1: [1,2,3,1], 2: [1,2,2,3,2], 3: [1,2,2,3,3,3]}
    assert update_AI(guess_hats, test_hat) == answer
#print(update_AI(guess_hats, test_hat))
