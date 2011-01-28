import ChessBoard

class FENGenerator:
    def __init__(self,initialFEN):
        self.FEN = initialFEN
        self.Board = ChessBoard.ChessBoard()
        self.MoveTurn = self.Board.MoveTurn
        
    def FENAfterMove(self,move):
        
        self.Board.MovePieceTo(move)
        self.FEN = self.Board.genFEN()
        return self.FEN
        


        
        
        

        
        
        
        
    
    
    
    
    
    
