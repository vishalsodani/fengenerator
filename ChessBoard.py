class ChessBoard:
    W = 'White'
    B = 'Black'
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
        
        

        self.Board[1][0] = self.WhitePawn
        self.Board[1][1] = self.WhitePawn
        self.Board[1][2] = self.WhitePawn
        self.Board[1][3] = self.WhitePawn
        self.Board[1][4] = self.WhitePawn
        self.Board[1][5] = self.WhitePawn
        self.Board[1][6] = self.WhitePawn
        self.Board[1][7] = self.WhitePawn

        self.Board[7][0] = self.BlackRook
        self.Board[7][1] = self.BlackKnight
        self.Board[7][2] = self.BlackBishop
        self.Board[7][3] = self.BlackQueen
        self.Board[7][4] = self.BlackKing
        self.Board[7][5] = self.BlackBishop
        self.Board[7][6] = self.BlackKnight
        self.Board[7][7] = self.BlackRook
        

        self.Board[6][0] = self.BlackPawn
        self.Board[6][1] = self.BlackPawn
        self.Board[6][2] = self.BlackPawn
        self.Board[6][3] = self.BlackPawn
        self.Board[6][4] = self.BlackPawn
        self.Board[6][5] = self.BlackPawn
        self.Board[6][6] = self.BlackPawn
        self.Board[6][7] = self.BlackPawn
        self.MoveTurn = self.W
        self.PawnCaptureByPawn = False
        self.currentfen = ''
        self.OriginalFile = []

    def genFEN(self):
        fen = ''
        EMPTYSQUARE = ''
        ALLSQUARES_EMPTY_INROW = 8
        startingrow = 7
        startingcol = 0
        emptySquaresCount = 0

        for rank in [7,6,5,4,3,2,1,0]:
            if rank < 7:
                fen += '/'
            for afile in range(startingcol,8):
                if self.Board[rank][afile] == EMPTYSQUARE:
                    emptySquaresCount += 1
                elif emptySquaresCount > 0 and self.Board[rank][afile] != EMPTYSQUARE:
                    fen += str(emptySquaresCount)
                    emptySquaresCount = 0
                    fen += self.Board[rank][afile]
                else:
                    fen += self.Board[rank][afile]
                if emptySquaresCount == ALLSQUARES_EMPTY_INROW:
                    fen += str(emptySquaresCount)
                    emptySquaresCount = 0
                elif emptySquaresCount > 0 and afile == 7 and self.Board[rank][afile] == EMPTYSQUARE:
                    fen += str(emptySquaresCount)
                    emptySquaresCount = 0
                   
        if self.MoveTurn == self.W:
            self.MoveTurn = self.B
        else:
            self.MoveTurn = self.W
        self.currentfen = fen
        return fen

    def evaluatePieceToMove(self,pieceToMove):
        if pieceToMove == 'P' and self.MoveTurn == self.W:
                movePiece = self.WhitePawn
        elif pieceToMove == 'P' and self.MoveTurn == self.B:
                movePiece = self.BlackPawn
        elif pieceToMove == 'N' and self.MoveTurn == self.W:
                movePiece = self.WhiteKnight
        elif pieceToMove == 'N' and self.MoveTurn == self.B:
                movePiece = self.BlackKnight
        elif pieceToMove == 'B' and self.MoveTurn == self.W:
                movePiece = self.WhiteBishop
        elif pieceToMove == 'B' and self.MoveTurn == self.B:
                movePiece = self.BlackBishop
        elif pieceToMove == 'Q' and self.MoveTurn == self.W:
                movePiece = self.WhiteQueen
        elif pieceToMove == 'Q' and self.MoveTurn == self.B:
                movePiece = self.BlackQueen
        elif pieceToMove == 'K' and self.MoveTurn == self.W:
                movePiece = self.WhiteKing
        elif pieceToMove == 'K' and self.MoveTurn == self.B:
                movePiece = self.BlackKing
        elif pieceToMove == 'R' and self.MoveTurn == self.W:
                movePiece = self.WhiteRook
        elif pieceToMove == 'R' and self.MoveTurn == self.B:
                movePiece = self.BlackRook
        return movePiece
    
    def MovePieceTo(self,move):
        #whats the piece, figure out original position n new position
        #parse first character of string to know the piece
        #whose move
        if move == '0-0' and self.MoveTurn == self.W:
            self.Board[0][4]=''
            self.Board[0][7]=''
            self.Board[0][5]=self.WhiteRook
            self.Board[0][6]=self.WhiteKing
        elif move == '0-0' and self.MoveTurn == self.B:
            self.Board[7][4]=''
            self.Board[7][7]=''
            self.Board[7][5]=self.BlackRook
            self.Board[7][6]=self.BlackKing
        else:    
            typeofpieceToMove = PieceParser().getPieceMoved(move)
            
            movePiece = self.evaluatePieceToMove(typeofpieceToMove)
            
            destSquare = self.getDestinationSquare(move,typeofpieceToMove)
            
            if typeofpieceToMove == Pieces.Pawn:
                orgSquare = self.getOriginalPosition(typeofpieceToMove,destSquare,move)
            else:
                orgSquare = self.getOriginalPositionForKnight(typeofpieceToMove,destSquare)
                
            self.Board[destSquare[0]][destSquare[1]] = movePiece
            if typeofpieceToMove == Pieces.Pawn:
                self.Board[orgSquare[0]][orgSquare[1]] = ''
            elif typeofpieceToMove == Pieces.Knight:
                print "for"
                if len(self.OriginalFile) == 1:
                    for pp in orgSquare:
                        if pp.filep == self.OriginalFile[0]:
                            self.Board[pp.rank][pp.filep]= ''
                        
                else:
                    
                    for pp in orgSquare:
                    
                        if (pp.filep - destSquare[1] == 1 or pp.filep - destSquare[1] == -1) and  abs(pp.rank - destSquare[0]) == 2:
                            print "1"
                            self.Board[pp.rank][pp.filep]=''
                        if destSquare[0] - pp.rank == 1 and  pp.filep - destSquare[1] == 2:
                            print "2"
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
                            print "here:"
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
                self.Board[whichrook.rank][whichrook.filep]=""
                            
                    
        
            
        

    def getOriginalPosition(self,piece,newsquare,move):
        #if its pawn can move one or 2 squares #which file how many pawns on that file
        fenranks = self.currentfen.split('/')
        
        fil = newsquare[1]
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
        
        return originalpos

    def getOriginalPositionForKnight(self,piece,newsquare):
        fenranks = self.currentfen.split('/')
        fenranks.reverse()
        
        fil = newsquare[1]
        ranks = []
        originalpos = []
        piecetolookfor = ''
        if piece == Pieces.Knight:
            if self.MoveTurn == self.W:
                piecetolookfor = 'N'
            else:
                piecetolookfor = 'n'
        if piece == Pieces.Bishop:
            if self.MoveTurn == self.W:
                piecetolookfor = 'B'
            else:
                piecetolookfor = 'b'
                   
        if piece == Pieces.Queen:
            if self.MoveTurn == self.W:
                piecetolookfor = 'Q'
            else:
                piecetolookfor = 'q'
        if piece == Pieces.King:
            if self.MoveTurn == self.W:
                piecetolookfor = 'K'
            else:
                piecetolookfor = 'k'
        if piece == Pieces.Rook:
            if self.MoveTurn == self.W:
                piecetolookfor = 'R'
            else:
                piecetolookfor = 'r'
            
        

        if piece == 'N' or piece == 'B' or piece == 'Q' or piece == 'K' or piece == 'R':
            
            for i in range(0,8):
                   filepos = 0 
                   for j in range(0,len(fenranks[i])):
                                  listpieces = fenranks[i]
                                  if listpieces[j].isdigit()== True:
                                     filepos +=  int(listpieces[j]) 
                                  if listpieces[j] == piecetolookfor:
                                      orgpos = PiecePosition(i,filepos)
                                      filepos += 1
                                      originalpos.append(orgpos)
                                  if listpieces[j].isdigit()== False and listpieces[j] != piecetolookfor:
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
                if len(move) == 4:
                    self.OriginalFile.append(self.Files.index(move[1]))
                    destFile = self.Files.index(move[2])
                    destRank = int(move[3])-1
                else:
                    destFile = self.Files.index(move[1])
                    destRank = int(move[2])-1
        destList.append(destRank)
        destList.append(destFile)
        return destList
            
class PiecePosition:

    def __init__(self,rank,filep):
        self.rank = rank
        self.filep = filep
class PieceParser:
    chessPiecesRepresentation = ['N','K','R','Q','B']
    def getPieceMoved(self,move):
                
        if move[0] in self.chessPiecesRepresentation:
            return self.chessPiecesRepresentation[self.chessPiecesRepresentation.index(move[0])] 
        else:
            return 'P'
class Pieces:
    Queen = 'Q'
    King = 'K'
    Rook ='R'
    Knight = 'N'
    Pawn = 'P'
    Bishop = 'B'
        
