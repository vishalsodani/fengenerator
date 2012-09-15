from Pieces import PieceParser
from Pieces import Pieces
from Pieces import PiecePosition
from FenBuilder import FenBuilder
import chessrules
import chessnotation
import Move


class ChessBoard:
    W = chessrules.is_white_move()
    B = chessrules.is_black_move()
    Files = ['a','b','c','d','e','f','g','h']

    def __init__(self,fen):

        self.Board = [["" for col in range(8)] for row in range(8)]
        self.setup_white_pieces()
        self.setup_black_pieces()
        self.MoveTurn = self.W
        self.currentfen = fen
       

        
    def setup_white_pieces(self):
        
        self.Board[0][0]= self.Board[0][7] = Pieces.WhiteRook
        self.Board[0][1] = self.Board[0][6] = Pieces.WhiteKnight
        self.Board[0][2] = self.Board[0][5]= Pieces.WhiteBishop
        self.Board[0][3] = Pieces.WhiteQueen
        self.Board[0][4] = Pieces.WhiteKing
        for bfile in range(0,8):
            self.Board[1][bfile] = Pieces.WhitePawn

    def setup_black_pieces(self):
        
        self.Board[7][0] = self.Board[7][7] = Pieces.BlackRook
        self.Board[7][1] = self.Board[7][6] = Pieces.BlackKnight
        self.Board[7][2] = self.Board[7][5] = Pieces.BlackBishop
        self.Board[7][3] = Pieces.BlackQueen
        self.Board[7][4] = Pieces.BlackKing
        for bfile in range(0,8):
            self.Board[6][bfile] = Pieces.BlackPawn

    def genFEN(self):
        
       
        startingcol = 0
        
        fenbuilder = FenBuilder(self.Board)
        for rank in range(7,-1,-1):
            if rank < 7:
                fenbuilder.fen += '/'
            for afile in range(startingcol,8):
                fenbuilder.build_fen_for_rank_file(rank,afile)  

        self.MoveTurn = self.B if self.MoveTurn == self.W else self.W

        self.currentfen = fenbuilder.fen
        return self.currentfen

   
    def is_square_empty(self,rank,afile):
        return self.Board[rank][afile] == ''
        
    def evaluatePieceToMove(self,pieceToMove):
        whitepieces = {Pieces.Pawn : Pieces.WhitePawn , Pieces.Knight : Pieces.WhiteKnight, Pieces.Bishop: Pieces.WhiteBishop, Pieces.Queen : Pieces.WhiteQueen,
                       Pieces.King : Pieces.WhiteKing, Pieces.Rook : Pieces.WhiteRook}
        blackpieces = {Pieces.Pawn : Pieces.BlackPawn , Pieces.Knight : Pieces.BlackKnight, Pieces.Bishop: Pieces.BlackBishop, Pieces.Queen : Pieces.BlackQueen,
                       Pieces.King : Pieces.BlackKing, Pieces.Rook : Pieces.BlackRook}

        
        return whitepieces[pieceToMove] if self.MoveTurn == self.W else blackpieces[pieceToMove]
       

    def remove_pawn_from_original_square(self,orgSquare):
        self.Board[orgSquare[0]][orgSquare[1]] = chessrules.make_square_blank()
        
    def remove_knight_from_original_square(self,orgSquare,destSquare,move):

            if Move.is_move_indicates_same2pieces_can_move(move):
                    for pp in orgSquare:
                        if pp.filep == self.Files.index(move[1]):
                            self.Board[pp.rank][pp.filep]= chessrules.make_square_blank()
                        
            else:

                    for pp in orgSquare:

                        if (pp.filep - destSquare[1] == 1 or pp.filep - destSquare[1] == -1) and  abs(pp.rank - destSquare[0]) == 2:
                            self.Board[pp.rank][pp.filep]=chessrules.make_square_blank()

                        if destSquare[0] - pp.rank == 1 and  pp.filep - destSquare[1] == 2:
                            self.Board[pp.rank][pp.filep]=chessrules.make_square_blank()

                        if abs(destSquare[0] - pp.rank) == 1 and  abs(pp.filep - destSquare[1]) == 2:
                            self.Board[pp.rank][pp.filep]=''
                            
    def remove_bishop_from_original_square(self,destSquare,orgSquare):

        # find if original square n destdquare are even or odd
                evensq = True
                if ((destSquare[0] + destSquare[1] + 7) % 2) != 0:
                    evensq = False
                
                for pp in orgSquare:
                    sum = pp.rank + pp.filep + 7
                    if  sum % 2 == 0 and evensq == True:
                        self.Board[pp.rank][pp.filep] = chessrules.make_square_blank()
                    elif sum % 2 != 0 and evensq == False:
                        self.Board[pp.rank][pp.filep] = chessrules.make_square_blank()
                        
    def remove_queen_from_original_square(self, orgSquare):
        self.Board[orgSquare[0].rank][orgSquare[0].filep]= ''

    def remove_rook_from_original_square(self, orgSquare, destSquare,move):

        originalrank = -1

        if Move.is_move_indicating_movement_of_onepiece_outofpossibility_of_two(move):
                    originalrank = int(move[1]) - 1

        
        if originalrank != -1:
                originalf = self.Files.index(move[2])
                self.Board[originalrank][originalf]=chessrules.make_square_blank()
        elif Move.is_move_indicates_same2pieces_can_move(move):
                    for rook in orgSquare:
                        if rook.filep == self.Files.index(move[1]):
                            self.Board[rook.rank][rook.filep]=chessrules.make_square_blank()
                            break

        elif len(orgSquare) >= 1:
                    
                    #is it horizontal movement, if both rooks are on same rank in original position
                    for rook in orgSquare:
                        diffsqrank = abs(rook.rank - destSquare[0])
                        diffsqfile = abs(rook.filep - destSquare[1])
                        if diffsqrank == 0 and diffsqfile == 1:
                            self.Board[rook.rank][rook.filep]=chessrules.make_square_blank()
                            break
                        elif diffsqrank == 0:
                            apieceexists = False
                            startLoop = rook.filep + 1
                            endLoop = diffsqfile
                            if (rook.filep  > destSquare[1]): #oh boy!! just check if rooks file is greater than dest file like Rf8 is greater than d8
                                startLoop = destSquare[1] + 1
                                endLoop = startLoop + diffsqfile - 1
                            for ifile in range(startLoop,endLoop):
                                if self.Board[rook.rank][ifile] != "":
                                    apieceexists = True
                                    break
                            if apieceexists == False:
                                    self.Board[rook.rank][rook.filep]=chessrules.make_square_blank()

                        #same file movement,vertical rook movement
                        elif diffsqfile == 0:
                            self.Board[rook.rank][rook.filep]=chessrules.make_square_blank()
                            break
               
       
        

    def handleWhiteKingSideCastling(self):
       self.Board[0][4]= self.Board[0][7]= chessrules.make_square_blank()
       self.Board[0][5]= Pieces.WhiteRook
       self.Board[0][6]= Pieces.WhiteKing
       
    def handleWhiteQueenSideCastling(self):
       self.Board[0][4]= self.Board[0][0]= chessrules.make_square_blank()
       self.Board[0][3]= Pieces.WhiteRook
       self.Board[0][2]= Pieces.WhiteKing
       
    def handleBlackKingSideCastling(self):
       self.Board[7][4]= self.Board[7][7]=chessrules.make_square_blank()
       self.Board[7][5]=  Pieces.BlackRook
       self.Board[7][6]=Pieces.BlackKing
       
    def handleBlackQueenSideCastling(self):
       self.Board[7][4]= self.Board[7][0]=chessrules.make_square_blank()
       self.Board[7][3]= Pieces.BlackRook
       self.Board[7][2]= Pieces.BlackKing
    
    def MovePieceTo(self,move):
        #whats the piece, figure out original position n new position
        #parse first character of string to know the piece
        #whose move
        if chessrules.is_white_kingside_castling(move,self.MoveTurn):
            self.handleWhiteKingSideCastling()
        elif chessrules.is_black_kingside_castling(move,self.MoveTurn):
            self.handleBlackKingSideCastling()
        elif chessrules.is_white_queenside_castling(move,self.MoveTurn):
            self.handleWhiteQueenSideCastling()
        elif chessrules.is_black_queenside_castling(move,self.MoveTurn):
            self.handleBlackQueenSideCastling()
        else:
            self.handleMove(move)
       

    def handleMove(self,move):

        typeofpieceToMove = PieceParser().getPieceMoved(move)
        piecetomove = self.evaluatePieceToMove(typeofpieceToMove)
        destSquare = Move.getDestinationSquare(move,typeofpieceToMove)
            
        if typeofpieceToMove == Pieces.Pawn:
            orgSquare = self.getOriginalPositionOfPawn(typeofpieceToMove,destSquare,move)
        else:
            orgSquare = self.getOriginalPositionForPiece(typeofpieceToMove,destSquare,piecetomove)
                
        self.Board[destSquare[0]][destSquare[1]] = piecetomove
            
        if typeofpieceToMove == Pieces.Pawn:
            self.remove_pawn_from_original_square(orgSquare)
        elif typeofpieceToMove == Pieces.Knight:
            self.remove_knight_from_original_square(orgSquare,destSquare,move)
        elif typeofpieceToMove == Pieces.Bishop:
             self.remove_bishop_from_original_square(destSquare,orgSquare)
        elif typeofpieceToMove == Pieces.Queen or typeofpieceToMove == Pieces.King:
             self.remove_queen_from_original_square(orgSquare)
        elif typeofpieceToMove == Pieces.Rook:
             self.remove_rook_from_original_square(orgSquare,destSquare,move)

        
       
    def get_file_of_newsquare(self,newsquare):
        
        return newsquare[1]
    
    def is_pawn_captured_by_pawn(self,pieceToMove,move):

        if pieceToMove != Pieces.Pawn:
            return False
        if chessnotation.CAPTURE_ACTION in move:
            return True
        return False
        
    def getOriginalPositionOfPawn(self,piece,newsquare,move):
        #if its pawn can move one or 2 squares #which file how many pawns on that file

        fil = self.get_file_of_newsquare(newsquare)
        ranks = []
        originalposofPawn = []
        ##for pawn
        PawnCaptureByPawn = self.is_pawn_captured_by_pawn(piece,move)
        NoOfPawnsInAFile = self.getNoOfPawnsInAFile(fil,ranks)
        #this is for enpassant if the destination square is empty,then take one rank abobe or below n make it empty
        if self.Board[newsquare[0]][newsquare[1]] == chessrules.make_square_blank() and PawnCaptureByPawn == True:
            if self.MoveTurn == self.B:
                self.Board[newsquare[0]+ 1][newsquare[1]]=chessrules.make_square_blank()
            elif self.MoveTurn == self.W:
                self.Board[newsquare[0]- 1][newsquare[1]]=chessrules.make_square_blank()	     


        if len(NoOfPawnsInAFile) == 1 and PawnCaptureByPawn == False:
            originalposofPawn.append(NoOfPawnsInAFile[0])
            originalposofPawn.append(fil)
        elif len(NoOfPawnsInAFile) == 1 and PawnCaptureByPawn == True and self.MoveTurn == self.B:
            #if self.Board[newsquare[0]][newsquare[1]]== chessrules.makesquare_blank(): #this is for enpassant if the destination square is empty
                #self.Board[newsquare[0]+ 1][newsquare[1]]=chessrules.makesquare_blank()
            originalposofPawn.append(newsquare[0] + 1)
            if move[2] > move[0]:
                originalposofPawn.append(fil - 1)
            else:
                originalposofPawn.append(fil + 1)
                
            
        elif len(NoOfPawnsInAFile) == 1 and PawnCaptureByPawn == True and self.MoveTurn == self.W:
            #if self.Board[newsquare[0]][newsquare[1]]== chessrules.makesquare_blank(): #this is for enpassant if the destination square is empty
                #self.Board[newsquare[0]- 1][newsquare[1]]=chessrules.makesquare_blank()

            originalposofPawn.append(newsquare[0] - 1)
            originalposofPawn.append(self.Files.index(move[0]))

        #this handles case when a pawn is captured ona file where there are no pawns of that color    
        elif len(NoOfPawnsInAFile) == 0 and PawnCaptureByPawn == True and self.MoveTurn == self.W:
            originalposofPawn.append(newsquare[0] - 1)
            originalposofPawn.append(self.Files.index(move[0]))
        elif len(NoOfPawnsInAFile) == 0 and PawnCaptureByPawn == True and self.MoveTurn == self.B:
            originalposofPawn.append(newsquare[0] + 1)
            originalposofPawn.append(self.Files.index(move[0]))
        elif len(NoOfPawnsInAFile) == 2:
            for rnk in ranks:
                if rnk -  newsquare[0]== 1 and self.MoveTurn == self.B or  rnk -  newsquare[0]== -1 and self.MoveTurn == self.W:
                    originalposofPawn.append(rnk)
                    originalposofPawn.append(fil)

       
        return originalposofPawn

    def getOriginalPositionForPiece(self,piece,newsquare,piecetomove):
        fenranks = self.currentfen.split('/')
        fenranks.reverse()
        
        fil = newsquare[1]
        ranks = []
        originalpos = []

        if piece != Pieces.Pawn:
            for i in range(0,8):
                   filepos = 0
                   for j in range(0,len(fenranks[i])):
                                  listpieces = fenranks[i]
                                  if listpieces[j].isdigit()== True:
                                     filepos +=  int(listpieces[j]) 
                                  if listpieces[j] == piecetomove:
                                      orgpos = PiecePosition(i,filepos)
                                      filepos += 1
                                      originalpos.append(orgpos)
                                  if listpieces[j].isdigit()== False and listpieces[j] != piecetomove:
                                      filepos += 1



        return originalpos
                                      

    def get_destination_file_rank_oncapture(self,move):
        return [self.Files.index(move[2]),int(move[3])-1]
    
    def get_destination_file_rank(self,move):
        return [self.Files.index(move[0]),int(move[1])-1]

   


    def getNoOfPawnsInAFile(self,bfile,ranks):

        [ranks.append(i) for i in range(0,8) if self.Board[i][bfile] == Pieces.WhitePawn and self.MoveTurn == self.W]
        [ranks.append(i) for i in range(0,8) if self.Board[i][bfile] == Pieces.BlackPawn and self.MoveTurn == self.B]
        return ranks
            

        
