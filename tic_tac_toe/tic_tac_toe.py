class TakenError(Exception):
    pass

class TicTacGame:
    def __init__(self):
        self.board = [[" "] * 3 for j in range(3)]

    def show_board(self):
        print(
            "{}|{}|{}\n-+-+-\n{}|{}|{}\n-+-+-\n{}|{}|{}".format(
                *self.board[0], *self.board[1], *self.board[2]
            )
        )
        return

    def validate_input(self):
        try:
            x, y = map(int, input().split())
            if x < 1 or x > 3 or y < 1 or y > 3:
                raise IndexError
            if self.board[x - 1][y - 1] != " ":
                raise TakenError
        except ValueError:
            raise
        return x, y

    def start_game(self):
        mark = "X"
        moves = 0
        while moves < 9:
            self.show_board()
            try:
                x, y = self.validate_input()
            except ValueError:
                print("Incorrect input")
                continue
            except IndexError:
                print("Out of grid")
                continue
            except TakenError:
                print("That place is already taken")
                continue
            self.board[x - 1][y - 1] = mark
            mark = "O" if (mark == "X") else "X"
            win = self.check_winner()
            if win == "X":
                self.show_board()
                print("first player won")
                return
            if win == "O":
                self.show_board()
                print("second player won")
                return
            moves += 1
        self.show_board()
        print("draw")
        return

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return 0


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
