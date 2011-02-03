from Pieces import PieceParser
from Pieces import Pieces
from Pieces import PiecePosition
from FenBuilder import FenBuilder
import chessrules


class ChessBoard:
    W = chessrules.itiswhites_move()
    B = chessrules.itisblacks_move()
    BlackPawn = 'p'
    WhitePawn = 'P'
    WhiteKing = 'K'
    BlackKing = 'k'
    WhiteRook = 'R'
    BlackRook = 'r'
    WhiteBishop = 'B'
    BlackBishop = 'b'
    WhiteQueen ='Q'
    BlackQueen = 'q'
    WhiteKnight = 'N'
    BlackKnight = 'n'
    
    
    Files = ['a','b','c','d','e','f','g','h']

    def __init__(self):
        self.Board = [['' for col in range(8)] for row in range(8)]
        self.Board[0][0] = self.WhiteRook
        self.Board[0][1] = self.WhiteKnight
        self.Board[0][2] = self.WhiteBishop
        self.Board[0][3] = self.WhiteQueen
        self.Board[0][4] = self.WhiteKing
        self.Board[0][5] = self.WhiteBishop
        self.Board[0][6] = self.WhiteKnight
        self.Board[0][7] = self.WhiteRook
        
        
        for bfile in range(0,8):
            self.Board[1][bfile] = self.WhitePawn


        self.Board[7][0] = self.BlackRook
        self.Board[7][1] = self.BlackKnight
        self.Board[7][2] = self.BlackBishop
        self.Board[7][3] = self.BlackQueen
        self.Board[7][4] = self.BlackKing
        self.Board[7][5] = self.BlackBishop
        self.Board[7][6] = self.BlackKnight
        self.Board[7][7] = self.BlackRook
        
        for bfile in range(0,8):
            self.Board[6][bfile] = self.BlackPawn

        self.MoveTurn = self.W
        self.PawnCaptureByPawn = False
        self.currentfen = ''
        self.OriginalFile = []
        self.piecetomove = ''

    def genFEN(self):
        
        EMPTYSQUARE = ''
        ALLSQUARES_EMPTY_INROW = 8
        startingrow = 7
        startingcol = 0
        
        fenbuilder = FenBuilder(self.Board)
        for rank in [7,6,5,4,3,2,1,0]:
            if rank < 7:
                fenbuilder.fen += '/'
            for afile in range(startingcol,8):

                if self.Board[rank][afile] == EMPTYSQUARE:
                    fenbuilder.build_fen_whenemptysqure()
                elif fenbuilder.emptySquaresCount > 0 and self.Board[rank][afile] != EMPTYSQUARE:
                    fenbuilder.build_fen_when_a_pieceexists_afteremptysquares(rank,afile)
                else:
                    fenbuilder.build_fen_when_a_pieceexists(rank,afile)
                    
                    
                #fenbuilder.build_fen_when_a_pieceexists_afteremptysquares(rank,afile) if fenbuilder.emptySquaresCount > 0 and self.Board[rank][afile] != EMPTYSQUARE
                if fenbuilder.emptySquaresCount == ALLSQUARES_EMPTY_INROW:
                    fenbuilder.fen += str(fenbuilder.emptySquaresCount)
                    fenbuilder.emptySquaresCount = 0
                elif fenbuilder.emptySquaresCount > 0 and afile == 7 and self.Board[rank][afile] == EMPTYSQUARE:
                    fenbuilder.fen += str(fenbuilder.emptySquaresCount)
                    fenbuilder.emptySquaresCount = 0
           


        self.MoveTurn = self.B if self.MoveTurn == self.W else self.W

        self.currentfen = fenbuilder.fen
        return self.currentfen

   
    
        
    def evaluatePieceToMove(self,pieceToMove):
        whitepieces = {Pieces.Pawn : self.WhitePawn , Pieces.Knight : self.WhiteKnight, Pieces.Bishop: self.WhiteBishop, Pieces.Queen : self.WhiteQueen,
                       Pieces.King : self.WhiteKing, Pieces.Rook : self.WhiteRook}
        blackpieces = {Pieces.Pawn : self.BlackPawn , Pieces.Knight : self.BlackKnight, Pieces.Bishop: self.BlackBishop, Pieces.Queen : self.BlackQueen,
                       Pieces.King : self.BlackKing, Pieces.Rook : self.BlackRook}

        
        return whitepieces[pieceToMove] if self.MoveTurn == self.W else blackpieces[pieceToMove]
       

   
    
    def MovePieceTo(self,move):
        #whats the piece, figure out original position n new position
        #parse first character of string to know the piece
        #whose move
        if chessrules.iswhite_kingside_castling(move,self.MoveTurn):
            self.Board[0][4]=self.Board[0][7]=chessrules.makesquare_blank()
            self.Board[0][5]=self.WhiteRook
            self.Board[0][6]=self.WhiteKing
        elif chessrules.isblack_kingside_castling(move,self.MoveTurn):
            self.Board[7][4]=self.Board[7][7]=chessrules.makesquare_blank()
            self.Board[7][5]=self.BlackRook
            self.Board[7][6]=self.BlackKing
        else:    
            typeofpieceToMove = PieceParser().getPieceMoved(move)
            
            self.piecetomove = self.evaluatePieceToMove(typeofpieceToMove)
            
            destSquare = self.getDestinationSquare(move,typeofpieceToMove)
     
            
            if typeofpieceToMove == Pieces.Pawn:
                orgSquare = self.getOriginalPosition(typeofpieceToMove,destSquare,move)
            else:
                orgSquare = self.getOriginalPositionForKnight(typeofpieceToMove,destSquare)
                
            self.Board[destSquare[0]][destSquare[1]] = self.piecetomove
            if typeofpieceToMove == Pieces.Pawn:
                self.Board[orgSquare[0]][orgSquare[1]] = ''
            elif typeofpieceToMove == Pieces.Knight:


                if len(self.OriginalFile) == 1:
                    for pp in orgSquare:
                        if pp.filep == self.OriginalFile[0]:
                            self.Board[pp.rank][pp.filep]= ''
                        
                else:
                    
                    for pp in orgSquare:
                    
                        if (pp.filep - destSquare[1] == 1 or pp.filep - destSquare[1] == -1) and  abs(pp.rank - destSquare[0]) == 2:
                            self.Board[pp.rank][pp.filep]=''
                        if destSquare[0] - pp.rank == 1 and  pp.filep - destSquare[1] == 2:
                
                            self.Board[pp.rank][pp.filep]=''
                        if abs(destSquare[0] - pp.rank == 1) and  abs(pp.filep - destSquare[1]) == 2:
                            self.Board[pp.rank][pp.filep]=''
            elif typeofpieceToMove == Pieces.Bishop:
                # find if original square n destdquare are even or odd
                evensq = True
                if ((destSquare[0] + destSquare[1] + 7) % 2) != 0:
                    evensq = False
                
                for pp in orgSquare:
                    sum = pp.rank + pp.filep + 7
                    if  sum % 2 == 0 and evensq == True:
                        self.Board[pp.rank][pp.filep] = ''
                    elif sum % 2 != 0 and evensq == False:
                        self.Board[pp.rank][pp.filep] = ''
            elif typeofpieceToMove == Pieces.Queen or typeofpieceToMove == Pieces.King:
                self.Board[orgSquare[0].rank][orgSquare[0].filep]= ''
            elif typeofpieceToMove == Pieces.Rook:

                if len(self.OriginalFile) == 1:
                    for rook in orgSquare:
                        if rook.filep == self.OriginalFile[0]:
                            whichrook = rook
                
                elif len(orgSquare) > 1:
                    
                    #is it horizontal movement, if both rooks are on same rank in original position
                    for rook in orgSquare:
                        whichrook = rook
                        diffsqrank = abs(rook.rank - destSquare[0])
                        diffsqfile = abs(rook.filep - destSquare[1])
                        if diffsqrank == 0 and diffsqfile == 1:
                            whichrook= rook
                            break
                        elif diffsqrank == 0:
                            for ifile in range(1,diffsqfile):
                                if self.Board[rook.rank][rook.filep + 1] != "":
                                    break
                                else:
                                    whichrook = rook
                        #same file movement,vertical rook movement
                        elif diffsqfile == 0:
                            whichrook = rook
                            break
                self.Board[whichrook.rank][whichrook.filep]=""
                            
                    
        
            
    def get_file_of_newsquare(self,newsquare):
        return newsquare[1]

    def getOriginalPosition(self,piece,newsquare,move):
        #if its pawn can move one or 2 squares #which file how many pawns on that file

        
        fil = self.get_file_of_newsquare(newsquare)
        ranks = []
        originalpos = []
        ##for pawn
        if piece == 'P':
            if self.MoveTurn == self.W:
                for i in range(0,8):
                    if self.Board[i][fil] == self.WhitePawn:
                        ranks.append(i)
            if self.MoveTurn == self.B:
                for i in range(0,8):
                    if self.Board[i][fil] == self.BlackPawn:
                        
                        ranks.append(i)
         
       
        if len(ranks) == 1 and self.PawnCaptureByPawn == False:
            originalpos.append(ranks[0])
            originalpos.append(fil)
        elif len(ranks) == 1 and self.PawnCaptureByPawn == True and self.MoveTurn == self.B:
       
            originalpos.append(newsquare[0] + 1)
            if move[2] > move[0]:
                originalpos.append(fil - 1)
            else:
                originalpos.append(fil + 1)
                
            
        elif len(ranks) == 1 and self.PawnCaptureByPawn == True and self.MoveTurn == self.W:
            originalpos.append(newsquare[0] - 1)
            originalpos.append(fil - 1)
        #this handles case when a pawn is captured ona file where there are no pawns of that color    
        elif len(ranks) == 0 and self.PawnCaptureByPawn == True and self.MoveTurn == self.W:
            originalpos.append(newsquare[0] - 1)
            originalpos.append(fil + 1)
        elif len(ranks) == 0 and self.PawnCaptureByPawn == True and self.MoveTurn == self.B:
            originalpos.append(newsquare[0] + 1)
            originalpos.append(fil - 1)
            
 
 
        
        
        return originalpos

    def getOriginalPositionForKnight(self,piece,newsquare):
        fenranks = self.currentfen.split('/')
        fenranks.reverse()
        
        fil = newsquare[1]
        ranks = []
        originalpos = []
        

            
        

        if piece == 'N' or piece == 'B' or piece == 'Q' or piece == 'K' or piece == 'R':
            
            for i in range(0,8):
                   filepos = 0 
                   for j in range(0,len(fenranks[i])):
                                  listpieces = fenranks[i]
                                  if listpieces[j].isdigit()== True:
                                     filepos +=  int(listpieces[j]) 
                                  if listpieces[j] == self.piecetomove:
                                      orgpos = PiecePosition(i,filepos)
                                      filepos += 1
                                      originalpos.append(orgpos)
                                  if listpieces[j].isdigit()== False and listpieces[j] != self.piecetomove:
                                      filepos += 1



        return originalpos
                                      
                                  
            
        
    def getDestinationSquare(self,move,pieceToMove):
        destList = []
        self.PawnCaptureByPawn = False
        self.OriginalFile=[]
        if pieceToMove == Pieces.Pawn:
            if 'x' in move:
                destFile = self.Files.index(move[2])
                destRank = int(move[3])-1
                self.PawnCaptureByPawn = True
            else:
                destFile = self.Files.index(move[0])
                destRank = int(move[1])-1
        
            
        else:
            if 'x' in move:
                destFile = self.Files.index(move[2])
                destRank = int(move[3])-1
        
            else:
                hasplus = '+' in move
                if len(move) == 4 and hasplus == False:
                    self.OriginalFile.append(self.Files.index(move[1]))
                    destFile = self.Files.index(move[2])
                    destRank = int(move[3])-1
                else:
                    destFile = self.Files.index(move[1])
                    destRank = int(move[2])-1
        destList.append(destRank)
        destList.append(destFile)
        return destList
            

        
