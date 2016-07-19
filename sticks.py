#W2D2

def get_game_sticks():
    while True:
        num = input("How many sticks would you like to begin with ?")
        if validate_input(num):
            return int(num)


def player1_choice():
    while True:
        pick = input("\nHow many sticks would you like to pick up? ")
        if validate_input(pick):
            if int(pick) in [1,2,3]:
                return int(pick)


def player2_choice():
    while True:
        pick = input("\nHow many sticks would you like to pick up? ")
        if validate_input(pick):
            if int(pick) in [1,2,3]:
                return int(pick)


def update_game(total_sticks):
    print("\n\nThere are now {} sticks left on the board".format(total_sticks))


def validate_input(data_in):
    if data_in.isdigit():
        return True
    else:
        return False


def main():
    while True:
        print('\n\n')
        print('*'*30)
        print('***\tPick-Up-Sticks     ***')
        print('*'*30)
        print('\n\n')

        total_sticks = get_game_sticks()

        update_game(total_sticks)

        sticks_picked = player1_choice()
        total_sticks -= sticks_picked
        update_game(total_sticks)
        sticks_picked = player2_choice()
        total_sticks -= sticks_picked


if __name__ == "__main__":
    main()
