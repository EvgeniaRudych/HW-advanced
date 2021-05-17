import unittest
from unittest.mock import patch
from game import TicTacToe


class TestWinner(unittest.TestCase):

    def setUp(self):
        self.tictac_test = TicTacToe()

    def test_winner_row_ind(self):
        self.tictac_test.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.tictac_test.print_board()
        self.assertTrue(self.tictac_test.winner(1, 'X'))
        self.tictac_test.board = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']
        self.tictac_test.print_board()
        self.assertFalse(self.tictac_test.winner(0, 'X'))

    def test_winner_col_ind(self):
        self.tictac_test.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.tictac_test.print_board()
        self.assertTrue(self.tictac_test.winner(3, 'X'))
        self.tictac_test.board = ['X', ' ', ' ', 'O', ' ', ' ', 'X', ' ', ' ']
        self.tictac_test.print_board()
        self.assertFalse(self.tictac_test.winner(0, 'X'))

    def test_winner_diagonal(self):
        self.tictac_test.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.tictac_test.print_board()
        self.assertTrue(self.tictac_test.winner(0, 'X'))
        self.tictac_test.board = ['X', ' ', ' ', ' ', 'O', ' ', ' ', ' ', 'X']
        self.tictac_test.print_board()
        self.assertFalse(self.tictac_test.winner(0, 'X'))

    if __name__ == '__main__':
        unittest.main()
