#W2D2

import random


def welcome_screen():
    print('\n\n')
    print('*'*30)
    print('***\tPick-Up-Sticks     ***')
    print('*'*30)
    print('\n\n')


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
        pick = input("\n\tPLAYER 1:  How many sticks would you like to pick up? ")
        if validate_input(pick):
            pick = int(pick)
            if pick in [1,2,3]:
                return pick


def player2_choice():
    while True:
        pick = input("\n\tPLAYER 2:  How many sticks would you like to pick up? ")
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


def computer_picks(hats, index, guess_hats):
    if index == 1:
        return 1
    choices = hats[index]               #choices is a list
    num = get_rand_num(len(choices))    #how many in list ? 3 is minimum
    print("\n\tPLAYER 2 chose to pick up {} sticks.".format(choices[num]))
    temp_tup = (index, choices[num])
    guess_hats.append(temp_tup)
    return choices[num]                 #return int at position: num


def get_rand_num(max):
    return random.randint(0, (max-1))


def update_AI(guess_hats, hats):
    for each in guess_hats:
        hats[each[0]].append(each[1])
    return hats
    print(guess_hats, "\n", hats)


#               ===================   MAIN   ===================              #

def main():

    hats = initialize_hats(60)
    keep_playing = True

#                        ======   GAME ENGINE   ======                        #
    while keep_playing:
        P1 = "won"
        P2 = "won"
        guess_hats = []

        welcome_screen()

        total_sticks = get_game_sticks()

        num_players = get_players()

        while True:
            update_game(total_sticks)

            sticks_picked = player1_choice()
            total_sticks -= sticks_picked

            update_game(total_sticks)

            if total_sticks <= 0:
                P1 = "lost"
                if num_players == 1:
                    update_AI(guess_hats, hats)
                break

            if num_players == 2:
                sticks_picked = player2_choice()
            else:
                sticks_picked = computer_picks(hats, total_sticks, guess_hats)

            total_sticks -= sticks_picked

            if total_sticks <= 0:
                P2 = "lost"
                print("\nAI was NOT updated.\n")
                break

        print("\n\nPlayer 1 {}\tPlayer 2 {}\n\n".format(P1,P2))

    entry = input("\nWould you like to play again? (Y/N) ")
    if entry == 'n' or entry == 'N':
        keep_playing = False


if __name__ == "__main__":
    main()
