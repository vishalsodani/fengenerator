import ChessBoard

class FENGenerator:
    def __init__(self, initial_fen):
        self.fen = initial_fen
        self.board = ChessBoard.ChessBoard(self.fen)
        self.move_turn = self.board.MoveTurn
        
    def fen_after_move(self, move):
        
        self.board.MovePieceTo(move)
        self.fen = self.board.genFEN()
        return self.fen
        


        
        
        

        
        
        
        
    
    
    
    
    
    
