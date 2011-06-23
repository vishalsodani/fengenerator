

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

    def build_fen_for_rank_file(self,rank,afile):

        EMPTYSQUARE = ''
        ALLSQUARES_EMPTY_INROW = 8
        
        if self.is_square_empty(rank,afile):
            self.build_fen_whenemptysqure()
        elif self.emptySquaresCount > 0 and self.is_square_empty(rank,afile) == False:
            self.build_fen_when_a_pieceexists_afteremptysquares(rank,afile)
        else:
            self.build_fen_when_a_pieceexists(rank,afile)
                    
                    
                #fenbuilder.build_fen_when_a_pieceexists_afteremptysquares(rank,afile) if fenbuilder.emptySquaresCount > 0 and self.Board[rank][afile] != EMPTYSQUARE
        if self.emptySquaresCount == ALLSQUARES_EMPTY_INROW or (self.emptySquaresCount > 0 and afile == 7 and self.board[rank][afile] == EMPTYSQUARE):
            self.fen += str(self.emptySquaresCount)
            self.emptySquaresCount = 0
        

    def is_square_empty(self,rank,afile):
        return self.board[rank][afile] == ''
    
