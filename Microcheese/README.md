# MISC - Micro Cheese
## 提示
Hint 說這題原本是 crypto，因為有 bug 所以放過來，因此可以跟原本的題目做個 diff

## diff
crypto 的 server.py 那邊第 36 行多了 else，也就是說這邊少判斷了一些東西導致出壞了
```
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
```

## 漏洞
如果直接在玩的時候輸入 0, 1, 2 以外的值，會導致 crash，這是因為 count 跟 pile 沒有給值就傳進去了。

所以要讓程式正常運作，又不能讓玩家這邊輸掉，就在一開始給很大的 count，導致程式在不會崩潰的情況下，又因為輸入太大的 count 而不動作，但是 AI 仍然會有動。

重複這個行為直到剩下一排的時候再全部取完就可以贏 AI 了

* flag: `AIS3{5._e3_b5_6._a4_Bb4_7._Bd2_a5_8._axb5_Bxc3}`
