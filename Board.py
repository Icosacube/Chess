import Piece
import tkinter as tk
import re
from tkinter import ttk

from collections.abc import Iterable

DIM_PATTERN = re.compile(r"(\d)x(\d)")
PIECE_PATTERN = re.compile(r"(\w+) (\d) (\d),(\d)")


class Board:
    """Board is mostly a 2d Array.
    Board can move pieces.
    Board has pieces. We assume 1 piece = 1 space.
    Board can be rendered."""

    # dim is an (x, y) tuple.
    def __init__(self, dim):
        assert(isinstance(dim, Iterable) and 
            isinstance(dim[0], int) and 
            isinstance(dim[1], int))
        self.x, self.y = dim

        self.boardState = [[None for j in range(self.y)] for i in range(self.x)]
    
    """add a piece to the board, if no piece exists at its current location."""
    def addPiece(self, newPiece):
        x, y = newPiece.getPos()
        if self.boardState[x][y] is None:
            self.boardState[x][y] = newPiece
    
    """Get whatever's at boardState[pos[0]][pos[1]]"""
    def getAt(self, pos):
        return self.boardState[pos[0]][pos[1]]
    
    """Delete a piece at a given space, if applicable."""
    def delPiece(self, pos):
        x, y = pos
        self.boardState[x][y] = None

    """Render the board in text. Notably, this board is on its side."""
    def render(self):
        print("   1 2 3 4 5 6 7 8 ")
        for i in range(self.x-1,-1,-1):
            print(f"{i+1} |",end="")
            for j in range(self.y):
                if (self.boardState[i][j] is None):
                    print("  ",end="")
                else:
                    print(f"{self.boardState[i][j]} ",end="")
            print("|")  # just a newline
    
    """
    Load in a board from filename.
    1st line should hold board dimensions, e.g. 8x8
    lines from then onwards should have piece names, colors and positions, e.g. pawn 0 1,1
    """
    @staticmethod
    def loadBoard(filename):
        isFirstLine = True
        board = None
        file = open(filename, 'r')

        line = file.readline()
        while (line):
            # get the board dimensions
            if isFirstLine:
                assert(board is None)
                match = DIM_PATTERN.search(line)
                x = int(match.group(1))
                y = int(match.group(2))

                board = Board((x, y))
                isFirstLine = False
            else: # add a piece to board
                assert(board is not None)
                match = PIECE_PATTERN.search(line)
                pieceName = match.group(1)
                color = Piece.COLORS[int(match.group(2))]
                x = int(match.group(3)) - 1
                y = int(match.group(4)) - 1

                if (pieceName.lower() == "pawn"):
                    newPiece = Piece.Pawn(color,(x,y))
                elif (pieceName.lower() == "knight"):
                    newPiece = Piece.Knight(color,(x,y))
                elif (pieceName.lower() == "bishop"):
                    newPiece = Piece.Bishop(color,(x,y))
                elif (pieceName.lower() == "rook"):
                    newPiece = Piece.Rook(color,(x,y))
                elif (pieceName.lower() == "queen"):
                    newPiece = Piece.Queen(color,(x,y))
                elif (pieceName.lower() == "king"):
                    newPiece = Piece.King(color,(x,y))
                
                board.addPiece(newPiece)

            line = file.readline()
        return board

    def isMoveValid(self, piecePos, pos2):
        piece = self.getAt(piecePos)
        assert(isinstance(piece, Piece))


    def isInBoard(self, pos):
        return (pos[0] > 0 and pos[0] < self.x and 
                pos[1] > 0 and pos[1] < self.y)
        
board = Board.loadBoard("defaultLayout.txt")
board.render()
input()