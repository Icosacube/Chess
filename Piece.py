import tkinter
from abc import ABC, abstractmethod
from collections.abc import Iterable

PROMO_ROW_WHT = 7
PROMO_ROW_BLK = 0
COLORS = ["white", "black"]

"""Abstract class detailing a chess piece."""
class AbstractPiece(ABC):    
    def __init__(self, color, pos):
        assert(isinstance(pos, Iterable) and 
               isinstance(pos[0], int) and 
               isinstance(pos[1], int))        
        self.color = color
        self.pos = pos
    
    def __repr__(self):
        return "ABSTRACT PIECE"
    
    def getPos(self):
        return self.pos

    """@abstractmethod
    def getZone(self, board):
        pass"""

    @abstractmethod
    def canMove(self, pos):
        pass

class Pawn(AbstractPiece):
    def __init__(self, color, pos):
        super().__init__(color, pos)
        self.hasMoved = False

    def __repr__(self):
        if self.color == "white":
            return "♙"
        elif self.color == "black":
            return "♟︎"

    def canMove(self, pos):
        # Check its own color and see if the new position is 1 step vertical or 1 step diagonal.
        super(pos)
        diffx = self.pos[0] - pos[0]
        diffy = self.pos[1] - pos[1]
        if not self.hasMoved:
            # check the two-step jump
            if (self.color == "white" and diffy == 2 and diffx == 0)\
                or (self.color == "black" and diffy == -2 and diffx == 0):
                return True
        
        return (self.color == "white")
    
    def canPromote(self):
        return (self.color == "white" and self.pos[1] == PROMO_ROW_WHT)\
            or (self.color == "black" and self.pos[1] == PROMO_ROW_BLK)

class Knight(AbstractPiece):
    def __repr__(self):
        if self.color == "white":
            return "♘"
        elif self.color == "black":
            return "♞"  

    def canMove(self, pos):
        # Check if the new position is either +-2 x and +- 1 y, or +-2 y and +- 1 x
        super(pos)
        diffx = self.pos[0] - pos[0]
        diffy = self.pos[1] - pos[1]
        return (abs(diffx) == 2 and abs(diffy) == 1)\
            or (abs(diffx) == 1 and abs(diffy) == 2)

class Bishop(AbstractPiece):
    def __repr__(self):
        if self.color == "white":
            return "♗"
        elif self.color == "black":
            return "♝"  

    def canMove(self, pos):
        # Check if the new position is on the same diagonal
        super(pos)
        diffx = self.pos[0] - pos[0]
        diffy = self.pos[1] - pos[1]
        return (abs(diffx) == abs(diffy))

class Rook(AbstractPiece):
    def __repr__(self):
        if self.color == "white":
            return "♖"
        elif self.color == "black":
            return "♜"  

    def canMove(self, pos):
        # Check if the new position is on same x or same y
        super(pos)
        return (pos[0] == self.pos[0] or pos[1] == self.pos[1])

class Queen(AbstractPiece):
    def __repr__(self):
        if self.color == "white":
            return "♕"
        elif self.color == "black":
            return "♛"  

    def canMove(self, pos):
        # Check if the new position is on same x or same y or same diagonal
        super(pos)
        diffx = self.pos[0] - pos[0]
        diffy = self.pos[1] - pos[1]
        return (pos[0] == self.pos[0] or pos[1] == self.pos[1]) or (abs(diffx) == abs(diffy))

class King(AbstractPiece):
    def __repr__(self):
        if self.color == "white":
            return "♔"
        elif self.color == "black":
            return "♚"

    def canMove(self, pos):
        # Check if new position is at most 1 different on xy coord
        super(pos)
        diffx = self.pos[0] - pos[0]
        diffy = self.pos[1] - pos[1]
        return (abs(diffx) == 1 and abs(diffy) == 1)

print("Piece.py imported.")