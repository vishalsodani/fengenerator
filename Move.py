import chessnotation
from Pieces import Pieces
Files = ['a','b','c','d','e','f','g','h']
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

def get_destination_file_rank_oncapture(move):
        return [Files.index(move[2]),int(move[3])-1]

def get_destination_file_rank(move):
        return [Files.index(move[0]),int(move[1])-1]

   
        
def getDestinationSquare(move,pieceToMove):
        
        destList = []
        if pieceToMove == Pieces.Pawn:
            if chessnotation.CAPTURE_ACTION in move:
                destFile , destRank = get_destination_file_rank_oncapture(move)
            else:
                destFile,destRank = get_destination_file_rank(move)
        else:
            if chessnotation.CAPTURE_ACTION in move:
                destFile , destRank = get_destination_file_rank_oncapture(move)
            else:
                
                if is_move_indicates_same2pieces_can_move(move):
                    destFile , destRank = get_destination_file_rank_oncapture(move)
                elif is_move_indicating_movement_of_onepiece_outofpossibility_of_two(move):
                    destFile , destRank = get_destination_file_rank_oncapture(move)
                else:
                    destFile = Files.index(move[1])
                    destRank = int(move[2])-1
        destList.append(destRank)
        destList.append(destFile)
        return destList
