import os
import random

def clr_scr():
    os.system("cls" if os.name == "nt" else "clear")

def pad_2(x):
    return f"{str(x):>2}"

class Minesweeper:
    def __init__(self):
        self._BOARD_WIDTH = 10
        self._BOARD_HEIGHT = 10
        self._MAX_MINES = self._BOARD_HEIGHT * self._BOARD_HEIGHT // 10 # 10% of the board will be mines
        self._board = []
    
    def _init_board(self):
        self._board = [[Minesweeper.__BoardTile() for _ in range(self._BOARD_WIDTH)] for _ in range(self._BOARD_HEIGHT)]
    
    def _print_board(self):
        if not self._board:
            raise Exception("Board is not initialized")
        
        clr_scr()

        # Header
        print(pad_2(" "), end=" ")
        for i in range(self._BOARD_WIDTH):
            print(pad_2(i), end=" ")
        print('\n', "-" * (self._BOARD_WIDTH * 3 + 1))

        # Board
        for row in range(self._BOARD_HEIGHT):
            print(pad_2(row), end="|")
            for x in self._board[row]:
                print(pad_2(x), end=" ")
            print()

    def _place_mines(self):
        mines = 0

        while mines < self._MAX_MINES:
            x = random.randrange(self._BOARD_WIDTH)
            y = random.randrange(self._BOARD_HEIGHT)

            while self._board[y][x].mined:
                x = random.randrange(self._BOARD_WIDTH)
                y = random.randrange(self._BOARD_HEIGHT)

            self._board[y][x].mined = True
            mines += 1

            # update neighbours

            self._update_neighbours(x, y)
        
    def _update_neighbours(self, x, y):
        neighbours = [ 
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)]
        
        for dx, dy in neighbours:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= self._BOARD_WIDTH or ny < 0 or ny >= self._BOARD_HEIGHT:
                continue

            self._board[ny][nx].value += 1

    
    def play(self):
        # init board
        self._init_board()
        # place mines
        self._place_mines()
        self._print_board()
        pass

    class __BoardTile:
        _MINE_TILE = 'X'
        _EMPTY_TILE = ' '

        def __init__(self, value = 0):
            self.value = value
            self.flagged = False
            self.mined = False

        def __str__(self):
            if self.mined:
                return self._MINE_TILE
            
            return str(self.value) if self.value else self._EMPTY_TILE

if __name__ == "__main__":
    ms = Minesweeper()
    ms.play()
