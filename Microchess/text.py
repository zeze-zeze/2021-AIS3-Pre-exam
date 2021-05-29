def print_welcome():
    print('+-------------------- welcome --------------------+')
    print('| omg hi!                                         |')
    print('|                                                 |')
    print('| welcome to microchess, the minimal online chess |')
    print('| platform.                                       |')
    print('| i am a super powerful chess AI!                 |')
    print('| can you win against me and get the flag?        |')


def print_flag(flag):
    print('+---------------- congratulations ----------------+')
    print('| you are a true grandmaster of chess! here is    |')
    print('| the flag for you:                               |')
    print('| ' + flag.ljust(47) + ' |')
    print('+-------------------------------------------------+')


def print_lose():
    print('+--------------------- oh no ---------------------+')
    print('| you lost against me! maybe try playing another  |')
    print('| match?                                          |')


def print_rules():
    print('+--------------------- rules ---------------------+')
    print('| since chess is a combinatorial game with quite  |')
    print('| complicated rules, my microchip is too micro to |')
    print('| handle it. instead, we shall play a simplified  |')
    print('| version of it:                                  |')
    print('|                                                 |')
    print('|  - the game starts with a few "piles".          |')
    print('|  - each pile has a positive number of "stones". |')
    print('|  - two players take turns. on each turn, the    |')
    print('|    player should choose a pile and remove any   |')
    print('|    positive number of stones from it.           |')
    print('|  - if all stones have been taken (so no moves   |')
    print('|    can be made), the current player loses and   |')
    print('|    the game ends.                               |')
    print('|                                                 |')
    print('| good luck!                                      |')


def print_game_menu():
    print('+---+--------------- game menu -------------------+')
    print('| 0 | make a move                                 |')
    print('| 1 | save the current game and leave             |')
    print('| 2 | resign the game                             |')
    print('+---+---------------------------------------------+')


def print_main_menu():
    print('+---+--------------- main menu -------------------+')
    print('| 0 | read the rules of the game                  |')
    print('| 1 | start a new game against me                 |')
    print('| 2 | load a saved game                           |')
    print('| 3 | leave                                       |')
    print('+---+---------------------------------------------+')


def print_move(person, count, pile):
    print('+--------------------- moved ---------------------+')
    print('| ' + f'{person} removed {count} stones from pile {pile}'.ljust(47) + ' |')


def print_error(error):
    print('+--------------------- error ---------------------+')
    print('| ' + error.ljust(47) + ' |')
