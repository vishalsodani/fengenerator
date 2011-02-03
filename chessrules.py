def iswhite_kingside_castling(move,moveturn):
    return move == 'O-O' and moveturn == itiswhites_move()
def isblack_kingside_castling(move,moveturn):
    return move == 'O-O' and moveturn == itisblacks_move()
def itiswhites_move():
    return 'White'
def itisblacks_move():
    return 'Black'
def makesquare_blank():
    return ''
