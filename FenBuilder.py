

class FenBuilder:

    def __init__(self,board):
        self.fen = ""
        self.emptySquaresCount = 0
        self.board = board
    def build_fen_whenemptysqure(self):
        self.emptySquaresCount += 1
    def build_fen_when_a_pieceexists_afteremptysquares(self,rank,afile):
        self.fen += str(self.emptySquaresCount)
        self.emptySquaresCount = 0
        self.fen += self.board[rank][afile]
    def build_fen_when_a_pieceexists(self,rank, afile):
        self.fen += self.board[rank][afile]
    
