class PiecePosition:

    def __init__(self,rank,filep):
        self.rank = rank
        self.filep = filep
class PieceParser:
    chessPiecesRepresentation = ['N','K','R','Q','B']
    def getPieceMoved(self,move):
                
        if move[0] in self.chessPiecesRepresentation:
            return self.chessPiecesRepresentation[self.chessPiecesRepresentation.index(move[0])] 
        else:
            return 'P'
class Pieces:
    Queen = 'Q'
    King = 'K'
    Rook ='R'
    Knight = 'N'
    Pawn = 'P'
    Bishop = 'B'
