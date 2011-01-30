import unittest
import FENGenerator
import ChessBoard

class TestFENGenerator(unittest.TestCase):
    def test_justtesting(self):
        self.assertEqual(1,1)
    def test_genFEN_AfterInitialPosition(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        self.assertEqual('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR',FENGen.FEN)
    def test_AfterSecondMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        self.assertEqual('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR',FENGen.FEN)
        #print FENGen.Board.Board
    def test_AfterThirdMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        self.assertEqual('rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R',FENGen.FEN)
        #print FENGen.Board.Board
    def test_After4thMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('Nc6')
        self.assertEqual('r1bqkbnr/pp1ppppp/2n5/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R',FENGen.FEN)
    def test_After5thMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('Nc6')
        FENGen.FENAfterMove('Bb5')
        self.assertEqual('r1bqkbnr/pp1ppppp/2n5/1Bp5/4P3/5N2/PPPP1PPP/RNBQK2R',FENGen.FEN)
    def test_After6thMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('Nc6')
        FENGen.FENAfterMove('Bb5')
        FENGen.FENAfterMove('Nf6')
        self.assertEqual('r1bqkb1r/pp1ppppp/2n2n2/1Bp5/4P3/5N2/PPPP1PPP/RNBQK2R',FENGen.FEN)
    def test_After7thMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('Nc6')
        FENGen.FENAfterMove('Bb5')
        FENGen.FENAfterMove('Nf6')
        FENGen.FENAfterMove('Bf1')
        self.assertEqual('r1bqkb1r/pp1ppppp/2n2n2/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R',FENGen.FEN)
    def test_After8thMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('Nc6')
        FENGen.FENAfterMove('Bb5')
        FENGen.FENAfterMove('Nf6')
        FENGen.FENAfterMove('Bf1')
        FENGen.FENAfterMove('Nxe4')
        
        self.assertEqual('r1bqkb1r/pp1ppppp/2n5/2p5/4n3/5N2/PPPP1PPP/RNBQKB1R',FENGen.FEN)
    def test_ForWhiteKingSideCastling(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('Nc6')
        FENGen.FENAfterMove('Bb5')
        FENGen.FENAfterMove('Nf6')
        FENGen.FENAfterMove('O-O')
      
        self.assertEqual('r1bqkb1r/pp1ppppp/2n2n2/1Bp5/4P3/5N2/PPPP1PPP/RNBQ1RK1',FENGen.FEN)
    def test_ForWhiteQueenMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Qe2')
      
        self.assertEqual('rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPPQPPP/RNB1KBNR',FENGen.FEN)
    def test_ForBlackQueenMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Qe2')
        FENGen.FENAfterMove('Qc7')
      
        self.assertEqual('rnb1kbnr/ppqppppp/8/2p5/4P3/8/PPPPQPPP/RNB1KBNR',FENGen.FEN)
    def test_ForWhiteKingMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Qe2')
        FENGen.FENAfterMove('Qc7')
        FENGen.FENAfterMove('Kd1')
      
        self.assertEqual('rnb1kbnr/ppqppppp/8/2p5/4P3/8/PPPPQPPP/RNBK1BNR',FENGen.FEN)
    def test_ForBlackKingMove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Qe2')
        FENGen.FENAfterMove('Qc7')
        FENGen.FENAfterMove('Kd1')
        FENGen.FENAfterMove('Kd8')
      
        self.assertEqual('rnbk1bnr/ppqppppp/8/2p5/4P3/8/PPPPQPPP/RNBK1BNR',FENGen.FEN)

        
  
        
    def test_initalFEN(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        self.assertEqual('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w',FENGen.FEN)
        self.assertEqual('White',FENGen.MoveTurn)
    def test_CB(self):
        CB = ChessBoard.ChessBoard()
        self.assertEqual('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',CB.genFEN())
    def test_shouldGiveEmptyStringForPawnMove_e4(self):
        Par = ChessBoard.PieceParser()
        self.assertEqual('N',Par.getPieceMoved('Ne4'))
    def test_ForCaptureByBlackPawn(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('e5')
        FENGen.FENAfterMove('d4')
        FENGen.FENAfterMove('exd4')
  
        self.assertEqual('rnbqkbnr/pppp1ppp/8/8/3pP3/8/PPP2PPP/RNBQKBNR',FENGen.FEN)

    def test_ForCaptureByWhitePawn(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('e5')
        FENGen.FENAfterMove('d4')
        FENGen.FENAfterMove('d6')
        FENGen.FENAfterMove('dxe5')
  
        self.assertEqual('rnbqkbnr/ppp2ppp/3p4/4P3/4P3/8/PPP2PPP/RNBQKBNR',FENGen.FEN)
    def test_ForRookMoveHorizontally(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('d6')
        FENGen.FENAfterMove('Bc4')
        FENGen.FENAfterMove('e6')
        FENGen.FENAfterMove('O-O')
        FENGen.FENAfterMove('Be7')

        FENGen.FENAfterMove('Re1')

        
        self.assertEqual('rnbqk1nr/pp2bppp/3pp3/2p5/2B1P3/5N2/PPPP1PPP/RNBQR1K1',FENGen.FEN)
    def test_ForRookMoveVertically(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('d6')
        FENGen.FENAfterMove('Bc4')
        FENGen.FENAfterMove('e6')
        FENGen.FENAfterMove('O-O')
        FENGen.FENAfterMove('Be7')

        FENGen.FENAfterMove('Re1')
        FENGen.FENAfterMove('Nf6')
        FENGen.FENAfterMove('Re3')

        
        self.assertEqual('rnbqk2r/pp2bppp/3ppn2/2p5/2B1P3/4RN2/PPPP1PPP/RNBQ2K1',FENGen.FEN)
    def test_ForRookMoveHorizontally_When2RooksCanmove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('d6')
        FENGen.FENAfterMove('d4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R',FENGen.FEN)
        FENGen.FENAfterMove('cxd4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/8/3pP3/5N2/PPP2PPP/RNBQKB1R',FENGen.FEN)
        FENGen.FENAfterMove('Nxd4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/8/3NP3/8/PPP2PPP/RNBQKB1R',FENGen.FEN)
        #print FENGen.FEN
        FENGen.FENAfterMove('Nf6')
        #self.assertEqual('rnbqkb1r/pp2pppp/3p1n2/8/3NP3/8/PPP2PPP/RNBQKB1R',FENGen.FEN)
        FENGen.FENAfterMove('Nc3')
        self.assertEqual('rnbqkb1r/pp2pppp/3p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R',FENGen.FEN)
        FENGen.FENAfterMove('a6')
        FENGen.FENAfterMove('Be2')
        FENGen.FENAfterMove('e6')
        FENGen.FENAfterMove('O-O')
        FENGen.FENAfterMove('Be7')
        FENGen.FENAfterMove('a4')
        FENGen.FENAfterMove('Nc6')
        FENGen.FENAfterMove('Be3')
        FENGen.FENAfterMove('O-O')
        FENGen.FENAfterMove('f4')
        FENGen.FENAfterMove('Qc7')
        FENGen.FENAfterMove('Kh1')
        FENGen.FENAfterMove('Re8')
        FENGen.FENAfterMove('Bf3')
        FENGen.FENAfterMove('Nd7')
        FENGen.FENAfterMove('Qe1')
        FENGen.FENAfterMove('Bf8')
        FENGen.FENAfterMove('Qf2')
        FENGen.FENAfterMove('Rb8')
        FENGen.FENAfterMove('Rad1')
        FENGen.FENAfterMove('Nxd4')
        FENGen.FENAfterMove('Rfe1')
        print FENGen.FEN
        self.assertEqual('1rb1rbk1/1pqn1ppp/p2pp3/8/P2nPP2/2N1BB2/1PP2QPP/3RR2K',FENGen.FEN)
    def test_ForKnightMove_When2KnightsCanmove(self):
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('d6')
        FENGen.FENAfterMove('d4')

        FENGen.FENAfterMove('cxd4')

        FENGen.FENAfterMove('Nxd4')

        FENGen.FENAfterMove('Nf6')

        FENGen.FENAfterMove('Nc3')
        FENGen.FENAfterMove('a6')
        FENGen.FENAfterMove('Ncb5')
        self.assertEqual('rnbqkb1r/1p2pppp/p2p1n2/1N6/3NP3/8/PPP2PPP/R1BQKB1R',FENGen.FEN)

    def test_ForWholeGame(self):
        
        FENGen = FENGenerator.FENGenerator('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w')
        FENGen.FENAfterMove('e4')
        FENGen.FENAfterMove('c5')
        FENGen.FENAfterMove('Nf3')
        FENGen.FENAfterMove('d6')
        FENGen.FENAfterMove('d4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/2p5/3PP3/5N2/PPP2PPP/RNBQKB1R',FENGen.FEN)
        FENGen.FENAfterMove('cxd4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/8/3pP3/5N2/PPP2PPP/RNBQKB1R',FENGen.FEN)
        FENGen.FENAfterMove('Nxd4')
        #self.assertEqual('rnbqkbnr/pp2pppp/3p4/8/3NP3/8/PPP2PPP/RNBQKB1R',FENGen.FEN)
        #print FENGen.FEN
        FENGen.FENAfterMove('Nf6')
        #self.assertEqual('rnbqkb1r/pp2pppp/3p1n2/8/3NP3/8/PPP2PPP/RNBQKB1R',FENGen.FEN)
        FENGen.FENAfterMove('Nc3')
        self.assertEqual('rnbqkb1r/pp2pppp/3p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R',FENGen.FEN)
        FENGen.FENAfterMove('a6')
        FENGen.FENAfterMove('Be2')
        FENGen.FENAfterMove('e6')
        FENGen.FENAfterMove('O-O')
        FENGen.FENAfterMove('Be7')
        FENGen.FENAfterMove('a4')
        FENGen.FENAfterMove('Nc6')
        FENGen.FENAfterMove('Be3')
        FENGen.FENAfterMove('O-O')
        FENGen.FENAfterMove('f4')
        FENGen.FENAfterMove('Qc7')
        FENGen.FENAfterMove('Kh1')
        FENGen.FENAfterMove('Re8')
        FENGen.FENAfterMove('Bf3')
        FENGen.FENAfterMove('Nd7')
        FENGen.FENAfterMove('Qe1')
        FENGen.FENAfterMove('Bf8')
        FENGen.FENAfterMove('Qf2')
        FENGen.FENAfterMove('Rb8')
        FENGen.FENAfterMove('Rad1')
        FENGen.FENAfterMove('Nxd4')
        FENGen.FENAfterMove('Bxd4')
        FENGen.FENAfterMove('b6')
        FENGen.FENAfterMove('e5')
        FENGen.FENAfterMove('dxe5')
        self.assertEqual('1rb1rbk1/2qn1ppp/pp2p3/4p3/P2B1P2/2N2B2/1PP2QPP/3R1R1K',FENGen.FEN)
        FENGen.FENAfterMove('fxe5')
        self.assertEqual('1rb1rbk1/2qn1ppp/pp2p3/4P3/P2B4/2N2B2/1PP2QPP/3R1R1K',FENGen.FEN)
        FENGen.FENAfterMove('Bc5')
        self.assertEqual('1rb1r1k1/2qn1ppp/pp2p3/2b1P3/P2B4/2N2B2/1PP2QPP/3R1R1K',FENGen.FEN)
        FENGen.FENAfterMove('Bh5')
        self.assertEqual('1rb1r1k1/2qn1ppp/pp2p3/2b1P2B/P2B4/2N5/1PP2QPP/3R1R1K',FENGen.FEN)
        FENGen.FENAfterMove('Rf8')
        self.assertEqual('1rb2rk1/2qn1ppp/pp2p3/2b1P2B/P2B4/2N5/1PP2QPP/3R1R1K',FENGen.FEN)
        FENGen.FENAfterMove('Bxf7+')
        self.assertEqual('1rb2rk1/2qn1Bpp/pp2p3/2b1P3/P2B4/2N5/1PP2QPP/3R1R1K',FENGen.FEN)
        FENGen.FENAfterMove('Kh8')
        FENGen.FENAfterMove('Ne4')

        FENGen.FENAfterMove('Nxe5')
        FENGen.FENAfterMove('Nxc5')
        FENGen.FENAfterMove('bxc5')
        self.assertEqual('1rb2r1k/2q2Bpp/p3p3/2p1n3/P2B4/8/1PP2QPP/3R1R1K',FENGen.FEN)
        FENGen.FENAfterMove('Bxe5')
        FENGen.FENAfterMove('Qxe5')
        FENGen.FENAfterMove('Bg6')
        FENGen.FENAfterMove('Rg8')
        FENGen.FENAfterMove('Bxh7')
        FENGen.FENAfterMove('Kxh7')
       

        FENGen.FENAfterMove('Qh4+')
        self.assertEqual('1rb3r1/6pk/p3p3/2p1q3/P6Q/8/1PP3PP/3R1R1K',FENGen.FEN)
        FENGen.FENAfterMove('Kg6')
        FENGen.FENAfterMove('Rd3')
        self.assertEqual('1rb3r1/6p1/p3p1k1/2p1q3/P6Q/3R4/1PP3PP/5R1K',FENGen.FEN)
        FENGen.FENAfterMove('Qh5')
        FENGen.FENAfterMove('Rg3+')

        self.assertEqual('1rb3r1/6p1/p3p1k1/2p4q/P6Q/6R1/1PP3PP/5R1K',FENGen.FEN)
        

        
        
        

        
if __name__ == '__main__':
    unittest.main()
