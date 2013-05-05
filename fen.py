import chess_board

class FENGenerator:
    def __init__(self, initial_fen):
        self.fen = initial_fen
        self.board = chess_board.ChessBoard(self.fen)
        self.move_turn = self.board.moveturn
        
    def fen_after_move(self, move):
        
        self.board.MovePieceTo(move)
        self.fen = self.board.generate_fen()
        return self.fen
        


        
        
        

        
        
        
        
    
    
    
    
    
    
