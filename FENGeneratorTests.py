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
        FENGen.FENAfterMove('0-0')
      
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

        
if __name__ == '__main__':
    unittest.main()
