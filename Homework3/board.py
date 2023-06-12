from pieces import *

class Board:

    def __init__(self):
        self._pieces = None
        self.placePieces()

    def placePieces(self):
        self._pieces = {
            ('A',1) : Rook('White', self, ('A',1)),
            ('B',1) : Knight('White', self, ('B',1)),
            ('C',1) : Bishop('White', self, ('C',1)),
            ('D',1) : King('White', self, ('D',1)),
            ('E',1) : Queen('White', self, ('E',1)),
            ('F',1) : Bishop('White', self, ('F',1)),
            ('G',1) : Knight('White', self, ('G',1)),
            ('H',1) : Rook('White', self, ('H',1)),

            ('A',8) : Rook('Black', self, ('A',8)),
            ('B',8) : Knight('Black', self, ('B',8)),
            ('C',8) : Bishop('Black', self, ('C',8)),
            ('D',8) : King('Black', self, ('D',8)),
            ('E',8) : Queen('Black', self, ('E',8)),
            ('F',8) : Bishop('Black', self, ('F',8)),
            ('G',8) : Knight('Black', self, ('G',8)),
            ('H',8) : Rook('Black', self, ('H',8)),

            ('A',2) : Pawn('White', self, ('A',2)),
            ('B',2) : Pawn('White', self, ('B',2)),
            ('C',2) : Pawn('White', self, ('C',2)),
            ('D',2) : Pawn('White', self, ('D',2)),
            ('E',2) : Pawn('White', self, ('E',2)),
            ('F',2) : Pawn('White', self, ('F',2)),
            ('G',2) : Pawn('White', self, ('G',2)),
            ('H',2) : Pawn('White', self, ('H',2)),

            ('A',7) : Pawn('Black', self, ('A',7)),
            ('B',7) : Pawn('Black', self, ('B',7)),
            ('C',7) : Pawn('Black', self, ('C',7)),
            ('D',7) : Pawn('Black', self, ('D',7)),
            ('E',7) : Pawn('Black', self, ('E',7)),
            ('F',7) : Pawn('Black', self, ('F',7)),
            ('G',7) : Pawn('Black', self, ('G',7)),
            ('H',7) : Pawn('Black', self, ('H',7))
        }

    def setPiece(self, position, piece: Piece):
        if piece.checkMove(position):
            self._pieces[position] = piece
            self._pieces[piece.position] = None
            self._pieces.__delitem__(piece.position)
            piece.position = position
            return True
        return False;

    def getPiece(self, position):
        if self._pieces.__contains__(position):
            return self._pieces[position]
        else:
            return None

    def makeMove(self, startPosition, endPosition, player):
        if self._pieces.__contains__(startPosition) == False:
            return False
        if self._pieces.__contains__(endPosition) == False and player != self._pieces[startPosition].color:
            return False        
        return self.setPiece(endPosition, self._pieces[startPosition])

    def displayBoard(self):
        print('   (A)(B)(C)(D)(E)(F)(G)(H)')
        for i in range(8, 0, -1):
            row = [f'({i})']
            for j in range(1, 9):
                piece = self.getPiece((chr(64+j), i))
                if piece is not None:
                    row.append(f'[{piece.getIcon()}]')
                else:
                    row.append('[ ]')
            print(''.join(row))