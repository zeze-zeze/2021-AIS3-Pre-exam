import random
from typing import Tuple


class Game:
    '''
    a simple Nim game with normal rules.
    grundy's theorem: if nim_sum() is zero, then the player to move has a
    winning strategy. otherwise, the other player has a winning strategy.
    '''

    def __init__(self):
        self.stones = []

    def generate_winning_game(self) -> None:
        '''generate a game such that the first player has a winning strategy'''
        self.stones = []
        xor_sum = 0

        piles = random.randint(6, 8)
        for i in range(piles):
            self.stones.append(count := random.randint(1, 31))
            xor_sum ^= count

        if xor_sum == 0:
            self.stones.append(random.randint(1, 31))

    def generate_losing_game(self) -> None:
        '''generate a game such that the second player has a winning strategy'''
        self.stones = []
        xor_sum = 0

        piles = random.randint(6, 8)
        for i in range(piles):
            self.stones.append(count := random.randint(1, 31))
            xor_sum ^= count

        if xor_sum != 0:
            self.stones.append(xor_sum)

    def make_move(self, pile: int, count: int) -> bool:
        '''makes a move, returns whether the move is legal'''

        if pile not in range(0, len(self.stones)):
            return False
        if count not in range(1, self.stones[pile] + 1):
            return False

        self.stones[pile] -= count
        if self.stones[pile] == 0:
            self.stones.pop(pile)

        return True

    def nim_sum(self) -> int:
        xor_sum = 0
        for count in self.stones:
            xor_sum ^= count
        return xor_sum

    def ended(self) -> bool:
        '''
        checks if the game has ended, i.e., the player has no more moves.
        if True, the current player loses the game
        '''
        return len(self.stones) == 0

    def show(self) -> None:
        print('+---+-------------- stones info ------------------+')
        for pile, count in enumerate(self.stones):
            print(f'| {pile} | {"o" * count:<43} |')

    def load(self, game_str: str) -> None:
        '''loads a saved game from string'''
        self.stones = list(map(int, game_str.split(',')))

    def save(self) -> str:
        '''returns the current game as a string'''
        return ','.join(map(str, self.stones))


class AIPlayer:
    '''
    a perfect Nim player. if there exists a winning strategy for a game, this
    player will always win.
    '''

    def __init__(self):
        pass

    def get_move(self, game: Game) -> Tuple[int, int]:
        '''
        if there is a winning strategy, returns a move that guarantees a win.
        otherwise, returns a random move.
        '''
        nim_sum = game.nim_sum()

        if nim_sum == 0:
            # losing game, make a random move
            pile = random.randint(0, len(game.stones) - 1)
            count = random.randint(1, game.stones[pile])

        else:
            # winning game, make a winning move
            for i, v in enumerate(game.stones):
                target = v ^ nim_sum
                if target < v:
                    pile = i
                    count = v - target
                    break

        return (pile, count)
