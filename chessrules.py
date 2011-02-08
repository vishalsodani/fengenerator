import chessnotation

def iswhite_kingside_castling(move,moveturn):
    return move == chessnotation.CASTLING_ACTION and moveturn == itiswhites_move()
def isblack_kingside_castling(move,moveturn):
    return move == chessnotation.CASTLING_ACTION and moveturn == itisblacks_move()
def itiswhites_move():
    return 'White'
def itisblacks_move():
    return 'Black'
def makesquare_blank():
    return ''
def iswhite_queenside_castling(move,moveturn):
    return move == chessnotation.QUEEN_CASTLING_ACTION and moveturn == itiswhites_move()
def isblack_queenside_castling(move,moveturn):
    return move == chessnotation.QUEEN_CASTLING_ACTION and moveturn == itisblacks_move()



