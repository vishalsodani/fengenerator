from pieces import PieceParser
from pieces import Pieces
from pieces import PiecePosition
from fen_builder import FenBuilder
import chessrules
import chessnotation
import move


class ChessBoard:
    W = chessrules.is_white_move()
    B = chessrules.is_black_move()
    Files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self,fen):

        self.board = [["" for col in range(8)] for row in range(8)]
        self.setup_white_pieces()
        self.setup_black_pieces()
        self.moveturn = self.W
        self.currentfen = fen



    def setup_white_pieces(self):

        self.board[0][0]= self.board[0][7] = Pieces.WhiteRook
        self.board[0][1] = self.board[0][6] = Pieces.WhiteKnight
        self.board[0][2] = self.board[0][5]= Pieces.WhiteBishop
        self.board[0][3] = Pieces.WhiteQueen
        self.board[0][4] = Pieces.WhiteKing
        for bfile in range(0,8):
            self.board[1][bfile] = Pieces.WhitePawn

    def setup_black_pieces(self):

        self.board[7][0] = self.board[7][7] = Pieces.BlackRook
        self.board[7][1] = self.board[7][6] = Pieces.BlackKnight
        self.board[7][2] = self.board[7][5] = Pieces.BlackBishop
        self.board[7][3] = Pieces.BlackQueen
        self.board[7][4] = Pieces.BlackKing
        for bfile in range(0,8):
            self.board[6][bfile] = Pieces.BlackPawn

    def generate_fen(self):


        startingcol = 0

        fenbuilder = FenBuilder(self.board)
        for rank in range(7,-1,-1):
            if rank < 7:
                fenbuilder.fen += '/'
            for afile in range(startingcol,8):
                fenbuilder.build_fen_for_rank_file(rank, afile)

        self.moveturn = self.B if self.moveturn == self.W else self.W

        self.currentfen = fenbuilder.fen
        return self.currentfen


    def is_square_empty(self, rank, afile):
        return self.board[rank][afile] == ''

    def evaluatePieceToMove(self, pieceToMove):
        whitepieces = {Pieces.Pawn : Pieces.WhitePawn ,
                       Pieces.Knight : Pieces.WhiteKnight,
                       Pieces.Bishop: Pieces.WhiteBishop,
                       Pieces.Queen : Pieces.WhiteQueen,
                       Pieces.King : Pieces.WhiteKing,
                       Pieces.Rook : Pieces.WhiteRook}
        blackpieces = {Pieces.Pawn : Pieces.BlackPawn ,
                       Pieces.Knight : Pieces.BlackKnight,
                       Pieces.Bishop: Pieces.BlackBishop,
                       Pieces.Queen : Pieces.BlackQueen,
                       Pieces.King : Pieces.BlackKing,
                       Pieces.Rook : Pieces.BlackRook}


        return whitepieces[pieceToMove] if self.moveturn == self.W \
               else blackpieces[pieceToMove]


    def remove_pawn_from_original_square(self, original_square):
        self.board[original_square[0]][original_square[1]] = chessrules.make_square_blank()

    def remove_knight_from_original_square(self, original_square,\
                                           destination_square, move_played):

        if move.is_move_indicates_same2pieces_can_move(move_played):
            for pp in original_square:
                if pp.filep == self.Files.index(move_played[1]):
                    self.board[pp.rank][pp.filep]= chessrules.make_square_blank()

        else:

            for pp in original_square:

                if (pp.filep - destination_square[1] == 1 or \
                    pp.filep - destination_square[1] == -1) and \
                    abs(pp.rank - destination_square[0]) == 2:
                    self.board[pp.rank][pp.filep]=chessrules.make_square_blank()

                if destination_square[0] - pp.rank == 1 and  pp.filep - destination_square[1] == 2:
                    self.board[pp.rank][pp.filep]=chessrules.make_square_blank()

                if abs(destination_square[0] - pp.rank) == 1 and  abs(pp.filep - destination_square[1]) == 2:
                    self.board[pp.rank][pp.filep]=''

    def remove_bishop_from_original_square(self, destination_square, original_square):




        # find if original square n destdquare are even or odd
        evensq = True
        if ((destination_square[0] + destination_square[1] + 7) % 2) != 0:
            evensq = False

        for pp in original_square:
            sum = pp.rank + pp.filep + 7
            if  sum % 2 == 0 and evensq == True:
                self.board[pp.rank][pp.filep] = chessrules.make_square_blank()
            elif sum % 2 != 0 and evensq == False:
                self.board[pp.rank][pp.filep] = chessrules.make_square_blank()

    def remove_queen_from_original_square(self, original_square):
        self.board[original_square[0].rank][original_square[0].filep]= ''

    def remove_rook_from_original_square(self, original_square, destination_square, move_played):

        originalrank = -1

        if move.is_move_indicating_movement_of_onepiece_outofpossibility_of_two(move_played):
            originalrank = int(move_played[1]) - 1


        if originalrank != -1:
            originalf = self.Files.index(move_played[2])
            self.board[originalrank][originalf]=chessrules.make_square_blank()
        elif move.is_move_indicates_same2pieces_can_move(move_played):
            for rook in original_square:
                if rook.filep == self.Files.index(move_played[1]):
                    self.board[rook.rank][rook.filep]=chessrules.make_square_blank()
                    break

        elif len(original_square) >= 1:

            #is it horizontal movement, if both rooks are on same rank in original position
            for rook in original_square:
                diffsqrank = abs(rook.rank - destination_square[0])
                diffsqfile = abs(rook.filep - destination_square[1])
                if diffsqrank == 0 and diffsqfile == 1:
                    self.board[rook.rank][rook.filep]=chessrules.make_square_blank()
                    break
                elif diffsqrank == 0:
                    apieceexists = False
                    start_loop = rook.filep + 1
                    end_loop = diffsqfile
                    if (rook.filep  > destination_square[1]): #oh boy!! just check if rooks file is greater than dest file like Rf8 is greater than d8
                        start_loop = destination_square[1] + 1
                        end_loop = start_loop + diffsqfile - 1
                    for ifile in range(start_loop,end_loop):
                        if self.board[rook.rank][ifile] != "":
                            apieceexists = True
                            break
                    if apieceexists == False:
                        self.board[rook.rank][rook.filep]=chessrules.make_square_blank()

                #same file movement,vertical rook movement
                elif diffsqfile == 0:
                    self.board[rook.rank][rook.filep]=chessrules.make_square_blank()
                    break




    def handle_white_king_side_castling(self):
        self.board[0][4] = self.board[0][7]= chessrules.make_square_blank()
        self.board[0][5] = Pieces.WhiteRook
        self.board[0][6] = Pieces.WhiteKing

    def handle_white_queen_side_castling(self):
        self.board[0][4] = self.board[0][0]= chessrules.make_square_blank()
        self.board[0][3] = Pieces.WhiteRook
        self.board[0][2] = Pieces.WhiteKing

    def handle_black_king_side_castling(self):
        self.board[7][4] = self.board[7][7]=chessrules.make_square_blank()
        self.board[7][5] = Pieces.BlackRook
        self.board[7][6] = Pieces.BlackKing

    def handle_black_queen_side_castling(self):
        self.board[7][4] = self.board[7][0]=chessrules.make_square_blank()
        self.board[7][3] = Pieces.BlackRook
        self.board[7][2] = Pieces.BlackKing

    def move_piece_to(self,move):
        #whats the piece, figure out original position n new position
        #parse first character of string to know the piece
        #whose move
        if chessrules.is_white_kingside_castling(move, self.moveturn):
            self.handle_white_king_side_castling()
        elif chessrules.is_black_kingside_castling(move, self.moveturn):
            self.handle_black_king_side_castling()
        elif chessrules.is_white_queenside_castling(move, self.moveturn):
            self.handle_white_queen_side_castling()
        elif chessrules.is_black_queenside_castling(move, self.moveturn):
            self.handle_black_queen_side_castling()
        else:
            self.handle_move(move)


    def handle_move(self, move_played):

        typeof_piece_to_move = PieceParser().getPieceMoved(move_played)
        piece_to_move = self.evaluatePieceToMove(typeof_piece_to_move)
        destination_square = move.getDestinationSquare(move_played,typeof_piece_to_move)

        if typeof_piece_to_move == Pieces.Pawn:
            original_square = self.getOriginalPositionOfPawn(typeof_piece_to_move,destination_square,move_played)
        else:
            original_square = self.getOriginalPositionForPiece(typeof_piece_to_move,destination_square,piece_to_move)

        self.board[destination_square[0]][destination_square[1]] = piece_to_move

        if typeof_piece_to_move == Pieces.Pawn:
            self.remove_pawn_from_original_square(original_square)
        elif typeof_piece_to_move == Pieces.Knight:
            self.remove_knight_from_original_square(original_square,destination_square,move_played)
        elif typeof_piece_to_move == Pieces.Bishop:
            self.remove_bishop_from_original_square(destination_square,original_square)
        elif typeof_piece_to_move == Pieces.Queen or typeof_piece_to_move == Pieces.King:
            self.remove_queen_from_original_square(original_square)
        elif typeof_piece_to_move == Pieces.Rook:
            self.remove_rook_from_original_square(original_square,destination_square,move_played)



    def get_file_of_newsquare(self, newsquare):

        return newsquare[1]

    def is_pawn_captured_by_pawn(self, pieceToMove, move):

        if pieceToMove != Pieces.Pawn:
            return False
        if chessnotation.CAPTURE_ACTION in move:
            return True
        return False

    def getOriginalPositionOfPawn(self, piece, newsquare, move):
        #if its pawn can move one or 2 squares #which file how many pawns on that file

        fil = self.get_file_of_newsquare(newsquare)
        ranks = []
        originalposofPawn = []
        ##for pawn
        PawnCaptureByPawn = self.is_pawn_captured_by_pawn(piece,move)
        NoOfPawnsInAFile = self.getNoOfPawnsInAFile(fil,ranks)
        #this is for enpassant if the destination square is empty,then take one rank abobe or below n make it empty
        if self.board[newsquare[0]][newsquare[1]] == chessrules.make_square_blank() and PawnCaptureByPawn == True:
            if self.moveturn == self.B:
                self.board[newsquare[0]+ 1][newsquare[1]] = chessrules.make_square_blank()
            elif self.moveturn == self.W:
                self.board[newsquare[0]- 1][newsquare[1]] = chessrules.make_square_blank()


        if len(NoOfPawnsInAFile) == 1 and PawnCaptureByPawn == False:
            originalposofPawn.append(NoOfPawnsInAFile[0])
            originalposofPawn.append(fil)
        elif len(NoOfPawnsInAFile) == 1 and PawnCaptureByPawn == True and self.moveturn == self.B:
            #if self.board[newsquare[0]][newsquare[1]]== chessrules.makesquare_blank(): #this is for enpassant if the destination square is empty
                #self.board[newsquare[0]+ 1][newsquare[1]]=chessrules.makesquare_blank()
            originalposofPawn.append(newsquare[0] + 1)
            if move[2] > move[0]:
                originalposofPawn.append(fil - 1)
            else:
                originalposofPawn.append(fil + 1)


        elif len(NoOfPawnsInAFile) == 1 and PawnCaptureByPawn == True and self.moveturn == self.W:
            #if self.board[newsquare[0]][newsquare[1]]== chessrules.makesquare_blank(): #this is for enpassant if the destination square is empty
                #self.board[newsquare[0]- 1][newsquare[1]]=chessrules.makesquare_blank()

            originalposofPawn.append(newsquare[0] - 1)
            originalposofPawn.append(self.Files.index(move[0]))

        #this handles case when a pawn is captured ona file where there are no pawns of that color
        elif len(NoOfPawnsInAFile) == 0 and PawnCaptureByPawn == True and self.moveturn == self.W:
            originalposofPawn.append(newsquare[0] - 1)
            originalposofPawn.append(self.Files.index(move[0]))
        elif len(NoOfPawnsInAFile) == 0 and PawnCaptureByPawn == True and self.moveturn == self.B:
            originalposofPawn.append(newsquare[0] + 1)
            originalposofPawn.append(self.Files.index(move[0]))
        elif len(NoOfPawnsInAFile) == 2:
            for rnk in ranks:
                if rnk -  newsquare[0] == 1 and self.moveturn == self.B or  rnk -  newsquare[0 ]== -1 and self.moveturn == self.W:
                    originalposofPawn.append(rnk)
                    originalposofPawn.append(fil)


        return originalposofPawn

    def getOriginalPositionForPiece(self, piece, newsquare, piecetomove):
        fenranks = self.currentfen.split('/')
        fenranks.reverse()

        fil = newsquare[1]
        ranks = []
        originalpos = []

        if piece != Pieces.Pawn:
            for i in range(0, 8):
                filepos = 0
                for j in range(0, len(fenranks[i])):
                    listpieces = fenranks[i]
                    if listpieces[j].isdigit()== True:
                        filepos +=  int(listpieces[j])
                    if listpieces[j] == piecetomove:
                        orgpos = PiecePosition(i, filepos)
                        filepos += 1
                        originalpos.append(orgpos)
                    if listpieces[j].isdigit()== False and listpieces[j] != piecetomove:
                        filepos += 1



        return originalpos


    def get_destination_file_rank_oncapture(self, move):
        return [self.Files.index(move[2]), int(move[3])-1]

    def get_destination_file_rank(self, move):
        return [self.Files.index(move[0]),int(move[1])-1]




    def getNoOfPawnsInAFile(self, bfile, ranks):

        [ranks.append(i) for i in range(0,8) if self.board[i][bfile] == Pieces.WhitePawn and self.moveturn == self.W]
        [ranks.append(i) for i in range(0,8) if self.board[i][bfile] == Pieces.BlackPawn and self.moveturn == self.B]
        return ranks
