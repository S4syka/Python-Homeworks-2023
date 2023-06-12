from board import Board
from pieces import *

class Chess:
    def __init__(self):
        self._currentPlayer = 'White'
        self._board = Board()

    def swapPlayers(self):
        if self._currentPlayer == 'White':
            self._currentPlayer = 'Black'
        if self._currentPlayer == 'Black':
            self._currentPlayer = 'White'
    
    def isStringValidMove(self, moveStr: str):
        if len(moveStr) != 2:
            return False;
        if ord(moveStr[0]) < ord('A') or ord(moveStr[0]) > ord('H'):
            return False;
        if ord(moveStr[1]) < ord('1') or ord(moveStr[1]) > ord('8'):
            return False;
        return True
    
    def play(self):
        while True:
            self._board.displayBoard()
            s = input()
            s = s.replace(" ", "")

            if self.isStringValidMove(s[:2]) == False or self.isStringValidMove(s[-2:]) == False or len(s) != 4:
                print("Invalid move, try again.")
                print(len(s))
                continue

            if self._board.makeMove((s[0], int(s[1])), (s[2], int(s[3])), self._currentPlayer):
                if self._currentPlayer == "White":
                    self._currentPlayer = "Black"
                else:
                    self._currentPlayer = "White"
                continue

            print("Invalid move, try again.1111")
        

if __name__ == "__main__":
    game = Chess()
    game.play() 