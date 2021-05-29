import myhash
from game import Game, AIPlayer
from text import *


flag = '(no flag here)'

hash = myhash.Hash()


def play(game: Game):
    ai_player = AIPlayer()
    win = False

    while not game.ended():
        game.show()
        print_game_menu()
        choice = input('it\'s your turn to move! what do you choose? ').strip()

        if choice == '0':
            pile = int(input('which pile do you choose? '))
            count = int(input('how many stones do you remove? '))
            if not game.make_move(pile, count):
                print_error('that is not a valid move!')
                continue

        elif choice == '1':
            game_str = game.save()
            digest = hash.hexdigest(game_str.encode())
            print('you game has been saved! here is your saved game:')
            print(game_str + ':' + digest)
            return

        elif choice == '2':
            break

        else:
            continue

        # no move -> player wins!
        if game.ended():
            win = True
            break
        else:
            print_move('you', count, pile)
            game.show()

        # the AI plays a move
        pile, count = ai_player.get_move(game)
        assert game.make_move(pile, count)
        print_move('i', count, pile)

    if win:
        print_flag(flag)
        exit(0)
    else:
        print_lose()


def menu():
    print_main_menu()
    choice = input('what would you like to do? ').strip()

    if choice == '0':
        print_rules()

    elif choice == '1':
        game = Game()
        game.generate_losing_game()
        play(game)

    elif choice == '2':
        saved = input('enter the saved game: ').strip()
        game_str, digest = saved.split(':')
        if hash.hexdigest(game_str.encode()) == digest:
            game = Game()
            game.load(game_str)
            play(game)
        else:
            print_error('invalid game provided!')

    elif choice == '3':
        print('omg bye!')
        exit(0)


if __name__ == '__main__':
    print_welcome()

    try:
        while True:
            menu()
    except Exception:
        print('oops i died')
