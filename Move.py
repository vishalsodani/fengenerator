import chessnotation

def is_it_a_check(move):
    is_check = chessnotation.CHECK_ACTION in move
    return is_check

def is_move_indicating_movement_of_onepiece_outofpossibility_of_two(move):
        if len(move) == 4 and is_it_a_check(move) == False and chessnotation.has2Digits(move) == True:
            return True
        return False

def is_move_indicates_same2pieces_can_move(move):

        if chessnotation.CAPTURE_ACTION in move:
            return False

        if len(move) == 4 and is_it_a_check(move) == False and chessnotation.has2Digits(move) == False:
            return True
        else:
            return False
