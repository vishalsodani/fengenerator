import unittest
import FENGenerator
import ChessBoard

class TestFENGenerator(unittest.TestCase):
    def test_justtesting(self):
        self.assertEqual(1,1)
    def test_genFEN_AfterInitialPosition(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        self.assertEqual('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR',FENGen.fen)
    def test_genFEN_AfterInitialPositionNf3(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('Nf3')
        self.assertEqual('rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R',FENGen.fen)
    def test_AfterSecondMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        self.assertEqual('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR',FENGen.fen)
        #print FENGen.121.board
    def test_AfterThirdMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        self.assertEqual('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R',FENGen.fen)
        #print FENGen.board.board
    def test_After4thMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('Nc6')
        self.assertEqual('r1bqkbnr/pp1ppppp/2n5/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R',FENGen.fen)
    def test_After5thMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('Nc6')
        FENGen.fen_after_move('Bb5')
        self.assertEqual('r1bqkbnr/pp1ppppp/2n5/1Bp5/4P3/5N2/PPPP1PPP/RNBQK2R',FENGen.fen)
    def test_After6thMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('Nc6')
        FENGen.fen_after_move('Bb5')
        FENGen.fen_after_move('Nf6')
        self.assertEqual('r1bqkb1r/pp1ppppp/2n2n2/1Bp5/4P3/5N2/PPPP1PPP/RNBQK2R',FENGen.fen)
    def test_After7thMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('Nc6')
        FENGen.fen_after_move('Bb5')
        FENGen.fen_after_move('Nf6')
        FENGen.fen_after_move('Bf1')
        self.assertEqual('r1bqkb1r/pp1ppppp/2n2n2/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R',FENGen.fen)
    def test_After8thMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('Nc6')
        FENGen.fen_after_move('Bb5')
        FENGen.fen_after_move('Nf6')
        FENGen.fen_after_move('Bf1')
        FENGen.fen_after_move('Nxe4')
        
        self.assertEqual('r1bqkb1r/pp1ppppp/2n5/2p5/4n3/5N2/PPPP1PPP/RNBQKB1R',FENGen.fen)
    def test_ForWhiteKingSideCastling(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('Nc6')
        FENGen.fen_after_move('Bb5')
        FENGen.fen_after_move('Nf6')
        FENGen.fen_after_move('O-O')
      
        self.assertEqual('r1bqkb1r/pp1ppppp/2n2n2/1Bp5/4P3/5N2/PPPP1PPP/RNBQ1RK1',FENGen.fen)
    def test_ForWhiteQueenMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Qe2')
      
        self.assertEqual('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPPQPPP/RNB1KBNR',FENGen.fen)
    def test_ForBlackQueenMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Qe2')
        FENGen.fen_after_move('Qc7')
      
        self.assertEqual('rnb1kbnr/ppqppppp/8/2p5/4P3/8/PPPPQPPP/RNB1KBNR',FENGen.fen)
    def test_ForWhiteKingMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Qe2')
        FENGen.fen_after_move('Qc7')
        FENGen.fen_after_move('Kd1')
      
        self.assertEqual('rnb1kbnr/ppqppppp/8/2p5/4P3/8/PPPPQPPP/RNBK1BNR',FENGen.fen)
    def test_ForBlackKingMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Qe2')
        FENGen.fen_after_move('Qc7')
        FENGen.fen_after_move('Kd1')
        FENGen.fen_after_move('Kd8')
      
        self.assertEqual('rnbk1bnr/ppqppppp/8/2p5/4P3/8/PPPPQPPP/RNBK1BNR',FENGen.fen)

        
  
        
    def test_initalFEN(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        self.assertEqual('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w',FENGen.fen)
        self.assertEqual('White',FENGen.board.MoveTurn)
    def test_CB(self):
        CB = ChessBoard.ChessBoard()
        self.assertEqual('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',CB.genFEN())
    def test_shouldGiveEmptyStringForPawnMove_e4(self):
        Par = ChessBoard.PieceParser()
        self.assertEqual('N',Par.getPieceMoved('Ne4'))
    def test_ForCaptureByBlackPawn(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('e5')
        FENGen.fen_after_move('d4')
        FENGen.fen_after_move('exd4')
  
        self.assertEqual('rnbqkbnr/pppp1ppp/8/8/3pP3/8/PPP2PPP/RNBQKBNR',FENGen.fen)

    def test_ForCaptureByWhitePawn(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('e5')
        FENGen.fen_after_move('d4')
        FENGen.fen_after_move('d6')
        FENGen.fen_after_move('dxe5')
  
        self.assertEqual('rnbqkbnr/ppp2ppp/3p4/4P3/4P3/8/PPP2PPP/RNBQKBNR',FENGen.fen)
    def test_ForRookMoveHorizontally(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('d6')
        FENGen.fen_after_move('Bc4')
        FENGen.fen_after_move('e6')
        FENGen.fen_after_move('O-O')
        FENGen.fen_after_move('Be7')

        FENGen.fen_after_move('Re1')

        
        self.assertEqual('rnbqk1nr/pp2bppp/3pp3/2p5/2B1P3/5N2/PPPP1PPP/RNBQR1K1',FENGen.fen)
    def test_ForRookMoveVertically(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('d6')
        FENGen.fen_after_move('Bc4')
        FENGen.fen_after_move('e6')
        FENGen.fen_after_move('O-O')
        FENGen.fen_after_move('Be7')

        FENGen.fen_after_move('Re1')
        FENGen.fen_after_move('Nf6')
        FENGen.fen_after_move('Re3')

        
        self.assertEqual('rnbqk2r/pp2bppp/3ppn2/2p5/2B1P3/4RN2/PPPP1PPP/RNBQ2K1',FENGen.fen)
    def test_ForRookMoveHorizontally_When2RooksCanmove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('d6')
        FENGen.fen_after_move('d4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R',FENGen.fen)
        FENGen.fen_after_move('cxd4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/8/3pP3/5N2/PPP2PPP/RNBQKB1R',FENGen.fen)
        FENGen.fen_after_move('Nxd4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/8/3NP3/8/PPP2PPP/RNBQKB1R',FENGen.fen)
        #print FENGen.fen
        FENGen.fen_after_move('Nf6')
        #self.assertEqual('rnbqkb1r/pp2pppp/3p1n2/8/3NP3/8/PPP2PPP/RNBQKB1R',FENGen.fen)
        FENGen.fen_after_move('Nc3')
        self.assertEqual('rnbqkb1r/pp2pppp/3p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R',FENGen.fen)
        FENGen.fen_after_move('a6')
        FENGen.fen_after_move('Be2')
        FENGen.fen_after_move('e6')
        FENGen.fen_after_move('O-O')
        FENGen.fen_after_move('Be7')
        FENGen.fen_after_move('a4')
        FENGen.fen_after_move('Nc6')
        FENGen.fen_after_move('Be3')
        FENGen.fen_after_move('O-O')
        FENGen.fen_after_move('f4')
        FENGen.fen_after_move('Qc7')
        FENGen.fen_after_move('Kh1')
        FENGen.fen_after_move('Re8')
        FENGen.fen_after_move('Bf3')
        FENGen.fen_after_move('Nd7')
        FENGen.fen_after_move('Qe1')
        FENGen.fen_after_move('Bf8')
        FENGen.fen_after_move('Qf2')
        FENGen.fen_after_move('Rb8')
        FENGen.fen_after_move('Rad1')
        FENGen.fen_after_move('Nxd4')
        FENGen.fen_after_move('Rfe1')
        
        self.assertEqual('1rb1rbk1/1pqn1ppp/p2pp3/8/P2nPP2/2N1BB2/1PP2QPP/3RR2K',FENGen.fen)
        
    def test_ForKnightMove_When2KnightsCanmove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('d6')
        FENGen.fen_after_move('d4')

        FENGen.fen_after_move('cxd4')

        FENGen.fen_after_move('Nxd4')

        FENGen.fen_after_move('Nf6')

        FENGen.fen_after_move('Nc3')
        FENGen.fen_after_move('a6')
        FENGen.fen_after_move('Ncb5')
        self.assertEqual('rnbqkb1r/1p2pppp/p2p1n2/1N6/3NP3/8/PPP2PPP/R1BQKB1R',FENGen.fen)

    def test_ForWholeGame(self):
        
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Nf3')
        FENGen.fen_after_move('d6')
        FENGen.fen_after_move('d4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R',FENGen.fen)
        FENGen.fen_after_move('cxd4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/8/3pP3/5N2/PPP2PPP/RNBQKB1R',FENGen.fen)
        FENGen.fen_after_move('Nxd4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/8/3NP3/8/PPP2PPP/RNBQKB1R',FENGen.fen)
        #print FENGen.fen
        FENGen.fen_after_move('Nf6')
        #self.assertEqual('rnbqkb1r/pp2pppp/3p1n2/8/3NP3/8/PPP2PPP/RNBQKB1R',FENGen.fen)
        FENGen.fen_after_move('Nc3')
        self.assertEqual('rnbqkb1r/pp2pppp/3p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R',FENGen.fen)
        FENGen.fen_after_move('a6')
        FENGen.fen_after_move('Be2')
        FENGen.fen_after_move('e6')
        FENGen.fen_after_move('O-O')
        FENGen.fen_after_move('Be7')
        FENGen.fen_after_move('a4')
        FENGen.fen_after_move('Nc6')
        FENGen.fen_after_move('Be3')
        FENGen.fen_after_move('O-O')
        FENGen.fen_after_move('f4')
        FENGen.fen_after_move('Qc7')
        FENGen.fen_after_move('Kh1')
        FENGen.fen_after_move('Re8')
        FENGen.fen_after_move('Bf3')
        FENGen.fen_after_move('Nd7')
        FENGen.fen_after_move('Qe1')
        FENGen.fen_after_move('Bf8')
        FENGen.fen_after_move('Qf2')
        FENGen.fen_after_move('Rb8')
        FENGen.fen_after_move('Rad1')
        FENGen.fen_after_move('Nxd4')
        FENGen.fen_after_move('Bxd4')
        FENGen.fen_after_move('b6')
        FENGen.fen_after_move('e5')
        FENGen.fen_after_move('dxe5')
        self.assertEqual('1rb1rbk1/2qn1ppp/pp2p3/4p3/P2B1P2/2N2B2/1PP2QPP/3R1R1K',FENGen.fen)
        FENGen.fen_after_move('fxe5')
        self.assertEqual('1rb1rbk1/2qn1ppp/pp2p3/4P3/P2B4/2N2B2/1PP2QPP/3R1R1K',FENGen.fen)
        FENGen.fen_after_move('Bc5')
        self.assertEqual('1rb1r1k1/2qn1ppp/pp2p3/2b1P3/P2B4/2N2B2/1PP2QPP/3R1R1K',FENGen.fen)
        FENGen.fen_after_move('Bh5')
        self.assertEqual('1rb1r1k1/2qn1ppp/pp2p3/2b1P2B/P2B4/2N5/1PP2QPP/3R1R1K',FENGen.fen)
        FENGen.fen_after_move('Rf8')
        self.assertEqual('1rb2rk1/2qn1ppp/pp2p3/2b1P2B/P2B4/2N5/1PP2QPP/3R1R1K',FENGen.fen)
        FENGen.fen_after_move('Bxf7+')
        self.assertEqual('1rb2rk1/2qn1Bpp/pp2p3/2b1P3/P2B4/2N5/1PP2QPP/3R1R1K',FENGen.fen)
        FENGen.fen_after_move('Kh8')
        FENGen.fen_after_move('Ne4')

        FENGen.fen_after_move('Nxe5')
        FENGen.fen_after_move('Nxc5')
        FENGen.fen_after_move('bxc5')
        self.assertEqual('1rb2r1k/2q2Bpp/p3p3/2p1n3/P2B4/8/1PP2QPP/3R1R1K',FENGen.fen)
        FENGen.fen_after_move('Bxe5')
        FENGen.fen_after_move('Qxe5')
        FENGen.fen_after_move('Bg6')
        FENGen.fen_after_move('Rg8')
        FENGen.fen_after_move('Bxh7')
        FENGen.fen_after_move('Kxh7')
       

        FENGen.fen_after_move('Qh4+')
        self.assertEqual('1rb3r1/6pk/p3p3/2p1q3/P6Q/8/1PP3PP/3R1R1K',FENGen.fen)
        FENGen.fen_after_move('Kg6')
        FENGen.fen_after_move('Rd3')
        self.assertEqual('1rb3r1/6p1/p3p1k1/2p1q3/P6Q/3R4/1PP3PP/5R1K',FENGen.fen)
        FENGen.fen_after_move('Qh5')
        FENGen.fen_after_move('Rg3+')

        self.assertEqual('1rb3r1/6p1/p3p1k1/2p4q/P6Q/6R1/1PP3PP/5R1K',FENGen.fen)


    def test_ForRookMoveHorizontally_When2RooksCanmove1(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('e6')
        FENGen.fen_after_move('f4')
        FENGen.fen_after_move('d5')
        FENGen.fen_after_move('e5')
       
        FENGen.fen_after_move('c5')
        
        FENGen.fen_after_move('Nf3')
      
        
        FENGen.fen_after_move('Nc6')
       
      
        
        FENGen.fen_after_move('Bb5')

        FENGen.fen_after_move('Bd7')
        FENGen.fen_after_move('Bxc6')
        FENGen.fen_after_move('Bxc6')
        FENGen.fen_after_move('O-O')
        
        FENGen.fen_after_move('Nh6')

        FENGen.fen_after_move('d3')
        FENGen.fen_after_move('Be7')
        FENGen.fen_after_move('Nc3')
        FENGen.fen_after_move('O-O')
        self.assertEqual('r2q1rk1/pp2bppp/2b1p2n/2ppP3/5P2/2NP1N2/PPP3PP/R1BQ1RK1',FENGen.fen)
        FENGen.fen_after_move('Ne2')
        FENGen.fen_after_move('f6')
        FENGen.fen_after_move('Ng3')
        FENGen.fen_after_move('Nf7')
        FENGen.fen_after_move('d4')
        FENGen.fen_after_move('cxd4')
        FENGen.fen_after_move('Nxd4')
        FENGen.fen_after_move('fxe5')

        FENGen.fen_after_move('Nxe6')
        FENGen.fen_after_move('Qb6+')
        FENGen.fen_after_move('Kh1')
        FENGen.fen_after_move('Bb5')
        FENGen.fen_after_move('Qg4')
        FENGen.fen_after_move('g6')
        FENGen.fen_after_move('f5')
        FENGen.fen_after_move('Bd7')
        FENGen.fen_after_move('Nxf8')
        self.assertEqual('r4Nk1/pp1bbn1p/1q4p1/3ppP2/6Q1/6N1/PPP3PP/R1B2R1K',FENGen.fen)
        FENGen.fen_after_move('Rxf8')
        
 
        
        #self.assertEqual('r4rk1/pp1bbn1p/1q2N1p1/3ppP2/6Q1/6N1/PPP3PP/R1B2R1K',FENGen.fen)
                #1. d4 d5 2. c4 c6 3. Nc3 Nf6 4. Nf3 e6 5. Bg5 dxc4 6. e4 b5 7. e5 h6
#8. Bh4 g5 9. Nxg5 hxg5 10. Bxg5 Nbd7 11. exf6 Bb7 12. g3 c5
    def test_gameva(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('d4')
        FENGen.fen_after_move('d5')
        FENGen.fen_after_move('c4')
        FENGen.fen_after_move('c6')
        FENGen.fen_after_move('Nc3')
       
        FENGen.fen_after_move('Nf6')
        
        FENGen.fen_after_move('Nf3')
      
        
        FENGen.fen_after_move('e6')
       
      
        
        FENGen.fen_after_move('Bg5')

        FENGen.fen_after_move('dxc4')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('b5')
        FENGen.fen_after_move('e5')
        
        FENGen.fen_after_move('h6')

        FENGen.fen_after_move('Bh4')
        FENGen.fen_after_move('g5')
        FENGen.fen_after_move('Nxg5')

        FENGen.fen_after_move('hxg5')

        
        

        FENGen.fen_after_move('Bxg5')

        FENGen.fen_after_move('Nbd7')
        FENGen.fen_after_move('exf6')

        FENGen.fen_after_move('Bb7')

        FENGen.fen_after_move('g3')
        

        FENGen.fen_after_move('c5')
        self.assertEqual('r2qkb1r/pb1n1p2/4pP2/1pp3B1/2pP4/2N3P1/PP3P1P/R2QKB1R',FENGen.fen)
        FENGen.fen_after_move('d5')
        FENGen.fen_after_move('Qb6')
        FENGen.fen_after_move('Bg2')
        FENGen.fen_after_move('O-O-O')
        FENGen.fen_after_move('O-O')
        FENGen.fen_after_move('b4')
        FENGen.fen_after_move('Na4')

        FENGen.fen_after_move('Qb5')
        FENGen.fen_after_move('a3')
        FENGen.fen_after_move('exd5')
        FENGen.fen_after_move('axb4')

        FENGen.fen_after_move('cxb4')
        FENGen.fen_after_move('Be3')
        FENGen.fen_after_move('Nc5')

        FENGen.fen_after_move('Qg4+')
        FENGen.fen_after_move('Rd7')
        FENGen.fen_after_move('Qg7')
        FENGen.fen_after_move('Bxg7')
        FENGen.fen_after_move('fxg7')

        FENGen.fen_after_move('Rg8')
        FENGen.fen_after_move('Nxc5')
        FENGen.fen_after_move('d4')
        FENGen.fen_after_move('Bxb7+')
        FENGen.fen_after_move('Rxb7')

        self.assertEqual('2k3r1/pr3pP1/8/1qN5/1ppp4/4B1P1/1P3P1P/R4RK1',FENGen.fen)
        

        
        


    def test_2whitepawansseparatedbyonerank(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('d6')
        FENGen.fen_after_move('f4')
        FENGen.fen_after_move('e5')
        self.assertEqual('rnbqkbnr/ppp2ppp/3p4/4p3/4PP2/8/PPPP2PP/RNBQKBNR',FENGen.fen)
        FENGen.fen_after_move('fxe5')
        self.assertEqual('rnbqkbnr/ppp2ppp/3p4/4P3/4P3/8/PPPP2PP/RNBQKBNR',FENGen.fen)   
        FENGen.fen_after_move('c6')
        self.assertEqual('rnbqkbnr/pp3ppp/2pp4/4P3/4P3/8/PPPP2PP/RNBQKBNR',FENGen.fen)
        FENGen.fen_after_move('e6')

        self.assertEqual('rnbqkbnr/pp3ppp/2ppP3/8/4P3/8/PPPP2PP/RNBQKBNR',FENGen.fen)
        
        FENGen.fen_after_move('Nf6')
        
      
        
        FENGen.fen_after_move('e5')
        
        self.assertEqual('rnbqkb1r/pp3ppp/2ppPn2/4P3/8/8/PPPP2PP/RNBQKBNR',FENGen.fen)

    def test_RooksOn_a5_and_a1_moveto_R1a3(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.fen_after_move('d4')
        FENGen.fen_after_move('d5')
        FENGen.fen_after_move('c4')
        FENGen.fen_after_move('c6')
        FENGen.fen_after_move('Nc3')
       
        FENGen.fen_after_move('Nf6')
        
        FENGen.fen_after_move('Nf3')
      
        
        FENGen.fen_after_move('e6')
       
      
        
        FENGen.fen_after_move('Bg5')

        FENGen.fen_after_move('dxc4')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('b5')
        FENGen.fen_after_move('e5')
        
        FENGen.fen_after_move('h6')

        FENGen.fen_after_move('Bh4')
        FENGen.fen_after_move('g5')
        FENGen.fen_after_move('Nxg5')

        FENGen.fen_after_move('hxg5')

        
        

        FENGen.fen_after_move('Bxg5')

        FENGen.fen_after_move('Nbd7')
        FENGen.fen_after_move('exf6')

        FENGen.fen_after_move('Bb7')

        FENGen.fen_after_move('g3')
        

        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('d5')
        FENGen.fen_after_move('Qb6')
        FENGen.fen_after_move('Bg2')
        FENGen.fen_after_move('O-O-O')
        FENGen.fen_after_move('O-O')
        FENGen.fen_after_move('b4')
        FENGen.fen_after_move('Na4')

        FENGen.fen_after_move('Qb5')
        FENGen.fen_after_move('a3')
        FENGen.fen_after_move('exd5')
        FENGen.fen_after_move('axb4')

        FENGen.fen_after_move('cxb4')
        FENGen.fen_after_move('Be3')
        FENGen.fen_after_move('Nc5')

        FENGen.fen_after_move('Qg4+')
        FENGen.fen_after_move('Rd7')
        FENGen.fen_after_move('Qg7')
        FENGen.fen_after_move('Bxg7')
        FENGen.fen_after_move('fxg7')

        FENGen.fen_after_move('Rg8')
        FENGen.fen_after_move('Nxc5')
        FENGen.fen_after_move('d4')
        FENGen.fen_after_move('Bxb7+')
        FENGen.fen_after_move('Rxb7')

        FENGen.fen_after_move('Ra5')
        FENGen.fen_after_move('f6')
        FENGen.fen_after_move('Rfa1')
        FENGen.fen_after_move('Re8')
        FENGen.fen_after_move('R5a3')

        self.assertEqual('2k1r3/pr4P1/5p2/1qN5/1ppp4/R3B1P1/1P3P1P/R5K1',FENGen.fen)
        



    
    def test_RooksOn(self):
            
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')

        
        FENGen.fen_after_move('d4')
        FENGen.fen_after_move('Nf6')
        FENGen.fen_after_move('c4')
        FENGen.fen_after_move('g6')
        FENGen.fen_after_move('Nc3')
        FENGen.fen_after_move('d5')

        FENGen.fen_after_move('cxd5')
        FENGen.fen_after_move('Nxd5')
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('Nxc3')
        FENGen.fen_after_move('bxc3')
        FENGen.fen_after_move('Bg7')
        FENGen.fen_after_move('Bc4')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('Ne2')
        FENGen.fen_after_move('Nc6')
        FENGen.fen_after_move('Be3')

        FENGen.fen_after_move('O-O')
        FENGen.fen_after_move('O-O')
        self.assertEqual('r1bq1rk1/pp2ppbp/2n3p1/2p5/2BPP3/2P1B3/P3NPPP/R2Q1RK1',FENGen.fen)

        FENGen.fen_after_move('Qc7')
        FENGen.fen_after_move('Rc1')
        self.assertEqual('r1b2rk1/ppq1ppbp/2n3p1/2p5/2BPP3/2P1B3/P3NPPP/2RQ1RK1',FENGen.fen)
        FENGen.fen_after_move('Rd8')

        self.assertEqual('r1br2k1/ppq1ppbp/2n3p1/2p5/2BPP3/2P1B3/P3NPPP/2RQ1RK1',FENGen.fen)

    def test_enpassant_blackpawncaptured(self):
            
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')

        
        FENGen.fen_after_move('e4')
        FENGen.fen_after_move('e6')
        FENGen.fen_after_move('e5')
       # FENGen.fen_after_move('f6')
        FENGen.fen_after_move('f5')
        FENGen.fen_after_move('exf6')
        

        self.assertEqual('rnbqkbnr/pppp2pp/4pP2/8/8/8/PPPP1PPP/RNBQKBNR',FENGen.fen)
        
    def test_enpassant_whitepawncaptured(self):
            
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')

        
        FENGen.fen_after_move('e3')
        FENGen.fen_after_move('c5')
        FENGen.fen_after_move('f3')
       # FENGen.fen_after_move('f6')
        FENGen.fen_after_move('c4')
        FENGen.fen_after_move('d4')
        FENGen.fen_after_move('cxd3')
        

        self.assertEqual('rnbqkbnr/pp1ppppp/8/8/8/3pPP2/PPP3PP/RNBQKBNR',FENGen.fen)


        
if __name__ == '__main__':
    unittest.main()
