import io
import unittest
from unittest.mock import patch
from tic_tac_toe import TicTacGame
from tic_tac_toe import TakenError


class TestGame(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show_board1(self, mock_stdout):
        game = TicTacGame()
        expected_output = " | | \n-+-+-\n | | \n-+-+-\n | | \n"
        game.show_board()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show_board2(self, mock_stdout):
        game = TicTacGame()
        expected_output = "X|X|X\n-+-+-\nX|X|X\n-+-+-\nX|X|X\n"
        game.board = [['X'] * 3 for j in range(3)]
        game.show_board()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_show_board3(self, mock_stdout):
        game = TicTacGame()
        expected_output = "O|O|O\n-+-+-\nO|O|O\n-+-+-\nO|O|O\n"
        game.board = [['O'] * 3 for j in range(3)]
        game.show_board()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1 2'])
    def test_validate_input1(self, _):
        game = TicTacGame()
        x, y = game.validate_input()
        self.assertEqual([x, y], [1, 2])

    @patch('builtins.input', side_effect=['1 20'])
    def test_validate_input2(self, _):
        game = TicTacGame()
        with self.assertRaises(IndexError):
            game.validate_input()

    @patch('builtins.input', side_effect=['1 2'])
    def test_validate_input3(self, _):
        game = TicTacGame()
        with self.assertRaises(TakenError):
            game.board[0][1] = 'X'
            game.validate_input()

    @patch('builtins.input', side_effect=['a'])
    def test_validate_input4(self, _):
        game = TicTacGame()
        with self.assertRaises(ValueError):
            game.validate_input()

    def test_check_winner1(self):
        game = TicTacGame()
        game.board[0][0] = 'X'
        game.board[1][1] = 'X'
        game.board[2][2] = 'X'
        self.assertEqual(game.check_winner(), 'X')

    def test_check_winner2(self):
        game = TicTacGame()
        game.board[1][0] = 'O'
        game.board[1][1] = 'O'
        game.board[1][2] = 'O'
        self.assertEqual(game.check_winner(), 'O')

    def test_check_winner3(self):
        game = TicTacGame()
        game.board[0][0] = 'X'
        game.board[1][1] = 'O'
        game.board[2][2] = 'X'
        self.assertEqual(game.check_winner(), 0)


if __name__ == '__main__':
    unittest.main()
