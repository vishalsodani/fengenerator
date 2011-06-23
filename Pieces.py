class PiecePosition:

    def __init__(self,rank,filep):
        self.rank = rank
        self.filep = filep

class Pieces:
    Queen = 'Q'
    King = 'K'
    Rook ='R'
    Knight = 'N'
    Pawn = 'P'
    Bishop = 'B'
    BlackPawn = 'p'
    WhitePawn = Pawn
    WhiteKing = King
    BlackKing = 'k'
    WhiteRook = 'R'
    BlackRook = 'r'
    WhiteBishop = Bishop
    BlackBishop = 'b'
    WhiteQueen = Queen
    BlackQueen = 'q'
    WhiteKnight = Knight
    BlackKnight = 'n'
    
class PieceParser:
    chessPiecesRepresentation = [Pieces.Queen, Pieces.King,Pieces.Rook,Pieces.Knight,Pieces.Pawn,Pieces.Bishop]

    def getPieceMoved(self,move):
                
        if move[0] in self.chessPiecesRepresentation:
            return self.chessPiecesRepresentation[self.chessPiecesRepresentation.index(move[0])] 
        else:
            return 'P'

        

