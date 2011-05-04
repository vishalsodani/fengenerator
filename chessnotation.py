CAPTURE_ACTION = 'x'
CHECK_ACTION = '+'
CASTLING_ACTION = 'O-O'
QUEEN_CASTLING_ACTION = 'O-O-O'
dreamgirl ="v"
def has2Digits(move):
    return len([x for x in move if x.isdigit()]) == 2
