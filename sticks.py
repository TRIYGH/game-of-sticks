#W2D2

import random

def get_game_sticks():
    while True:
        num = input("How many sticks would you like to begin with ?")
        if validate_input(num):
            return int(num)


def initialize_hats(sticks):
    counter = 1
    hat = {}

    while counter < (sticks+1):
        hat.update({counter: [1,2,3]})
        counter += 1
    return hat


def player1_choice():
    while True:
        pick = input("\nPLAYER 1:  How many sticks would you like to pick up? ")
        if validate_input(pick):
            pick = int(pick)
            if pick in [1,2,3]:
                return pick


def player2_choice():
    while True:
        pick = input("\nPLAYER 2:  How many sticks would you like to pick up? ")
        if validate_input(pick):
            pick = int(pick)
            if pick in [1,2,3]:
                return pick


def update_game(total_sticks):
    print("\n\nThere are now {} sticks left on the board".format(total_sticks))


def validate_input(data_in):
    if data_in.isdigit():
        return True
    else:
        return False


def get_players():
    while True:
        print("====  Choose your players  ====")
        print("(1) You against the Computer")
        entry = input("(2) Players                ")
        if validate_input(entry):
            return int(entry)


def computer_picks(hats, index):
    if index == 1:
        return 1
    choices = hats[index]               #choices is a list
    num = get_rand_num(len(choices))    #how many in list ? 3 is minimum
    return choices[num]                 #return int at position: num


def get_rand_num(max):
    return random.randint(0, max)


#               ===================   MAIN   ===================              #

def main():
    P1 = "won"
    P2 = "won"
    print('\n\n')
    print('*'*30)
    print('***\tPick-Up-Sticks     ***')
    print('*'*30)
    print('\n\n')

    total_sticks = get_game_sticks()

    num_players = get_players()
    if num_players == 1:
        hats = initialize_hats(total_sticks)



#                   ======   GAME ENGINE   ======                      #

    while True:
        update_game(total_sticks)

        sticks_picked = player1_choice()
        total_sticks -= sticks_picked

        update_game(total_sticks)

        if total_sticks <= 0:
            P1 = "lost"
            break

        if num_players == 2:
            sticks_picked = player2_choice()
        else:
            sticks_picked = computer_picks(hats, total_sticks)

        total_sticks -= sticks_picked

        if total_sticks <= 0:
            P2 = "lost"
            break

    print("\n\nPlayer 1 {}\tPlayer 2 {}\n\n".format(P1,P2))


if __name__ == "__main__":
    main()
