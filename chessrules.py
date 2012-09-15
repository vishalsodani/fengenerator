import chessnotation

def is_white_kingside_castling(move,moveturn):
    return move == chessnotation.CASTLING_ACTION and moveturn == is_white_move()
def is_black_kingside_castling(move,moveturn):
    return move == chessnotation.CASTLING_ACTION and moveturn == is_black_move()
def is_white_move():
    return 'White'
def is_black_move():
    return 'Black'
def make_square_blank():
    return ''
def is_white_queenside_castling(move,moveturn):
    return move == chessnotation.QUEEN_CASTLING_ACTION and moveturn == is_white_move()
def is_black_queenside_castling(move,moveturn):
    return move == chessnotation.QUEEN_CASTLING_ACTION and moveturn == is_black_move()



    



