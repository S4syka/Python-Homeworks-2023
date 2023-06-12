
blackIcons = {"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" }
whiteIcons = {"Pawn" : "♟", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" }

class Piece:
    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        self._position = value
    
    @property
    def board(self):
        return self._board
    
    def __init__(self, color: str, board, position):
        self._color = color
        self._position = position
        self._board = board


    def checkMove(self, dest): 
        return False

    def move(self, dest):
        if self.checkMove(dest) == True:
            self.position = dest
            return True
        return False
        
    def getName(self):
        return self.__class__.__name__

    def getIcon(self):
        if type(self) is Piece:
            return None
        elif self.color == "White":
            return whiteIcons[self.__class__.__name__]
        elif self.color == "Black":
            return blackIcons[self.__class__.__name__]
        
    def checkDiagonal(self, position):
        if self.position == position:
            return False

        if abs(ord(self[0].position) - ord(position[0])) != abs(self.position[1] - position[1]):
            return False;
        
        k1 = 1;
        k2 = 1;
        if ord(position[0]) < ord(self.position[0]):
            k1 = -1
        if position[1] < self.position[1]:
            k2 = -1

        for i in range(ord(self.position[0]), ord(position[0]), k1):
            for j in range(self.position[1], position[1], k2):
                if self.board.getPiece((chr(i), j)) != None:
                    return False
                
        if self.board.getPiece(position) == None:
            return True;
        elif self.board.getPiece(position).color() == self.color():
            return False;
        return True;

    def CheckHorizontalVertical(self, position):
        if self.position == position:
            return False
        
        if self.position[0] != position[0] and self.position[1] != position[1]:
            return False
        
        k = 1;
        if ord(position[0]) < ord(self.position[0]):
            k = -1
        
        for i in range(ord(self.position[0]), ord(position[0]), k):
            if self.board.getPiece((chr(i), position[1])) != None:
                return False
        k = 1;
        if position[1] < self.position[1]:
            k = -1

        for i in range(self.position[1], position[1]):
            if self.board.getPiece((position[0], i)) != None:
                return False
            
        if self.board.getPiece(position) == None:
                return True;
        elif self.board.getPiece(position).color() == self.color():
            return False;
        return True;







class Knight(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
    
    def checkMove(self, dest):
        if abs(ord(dest[0]) - ord(self._position[0])) == 1 and abs(dest[1] - self._position[1]) == 2 or abs(ord(dest[0]) - ord(self._position[0])) == 2 and abs(dest[1] - self._position[1]) == 1:
            if self.board.getPiece(dest) == None:
                return True;
            elif self.board.getPiece(dest).color() == self.color():
                return False;
            return True;
        return False
    

class Rook(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def checkMove(self, dest):
        return self.CheckHorizontalVertical(dest)
        
class Bishop(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def checkMove(self, dest):
        return self.checkDiagonal(dest)
        
class Queen(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def checkMove(self, dest):
        return self.checkDiagonal(dest) or self.CheckHorizontalVertical(dest)


class King(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
    
    def checkMove(self, dest):
        if(abs(ord(self.position[0]) - ord(dest[0])) > 1 or abs(self.position[1] - dest[1])) :
            return False;
    
        if self.board.getPiece(dest) == None:
                return True;
        elif self.board.getPiece(dest).color() == self.color():
            return False;
        return True;

class Pawn(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self._start = True
    
    def checkMove(self, dest):
        if self.color == 'White':
            if self._start == True and dest[0] == self.position[0] and dest[1] == 4 and self.board.getPiece(dest) == None:
                return True;
            if dest[0] == self.position[0] and dest[1] - self.position[1] == 1 and self.board.getPiece(dest) == None:
                return True
            if dest[1] - self.position[1] == 1 and abs(ord(dest[1] - self.position[1])) == 1 and self.board.getPiece(dest).color != self.color:
                return True;
            return False;
    
        if self.color == 'Black':
            if self._start == True and dest[0] == self.position[0] and dest[1] == 5 and self.board.getPiece(dest) == None:
                return True;
            if dest[0] == self.position[0] and dest[1] - self.position[1] == -1 and self.board.getPiece(dest) == None:
                return True
            if dest[1] - self.position[1] == -1 and abs(ord(dest[1] - self.position[1])) == 1 and self.board.getPiece(dest).color != self.color:
                return True;
            return False;

        return False;
    
    def Move(self, dest):
        if self.checkMove(dest) == True:
            self.position = dest
            self._start = False
            return True
        return False