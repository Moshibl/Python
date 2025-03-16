#1. Tic-Tac-Toe:
import os
def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')


class Board:
    def __init__(self):
        self.board = [['   ' for _ in range(3)] for _ in range(3)]

    def display(self):
        print('-------------')
        for row in self.board:
            print('|', '|'.join(row), '|', sep='')
            print('-------------')

    def update(self, row, col, symbol):
        if self.board[row][col] == '   ':
            self.board[row][col] = f' {symbol} '
            return True
        return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '   ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '   ':
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '   ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '   ':
            return self.board[0][2]

        return None

    def is_full(self):
        return all(self.board[i][j] != '   ' for i in range(3) for j in range(3))


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                row, col = map(int, input(f'Player {self.symbol}, enter your move (row col): ').split())
                if 0 <= row < 3 and 0 <= col < 3:
                    if board.update(row, col, self.symbol):
                        break
                    else:
                        print('That spot is already taken. Try again.')
                else:
                    print('Invalid move. Please enter row and column between 0 and 2.')
            except ValueError:
                print('Invalid input. Please enter two integers for row and column.')


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.current_player = self.player1

    def play(self):
        clear_console()
        while True:
            self.board.display()

            self.current_player.make_move(self.board)
            clear_console()

            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f'Player {winner} wins!')
                break

            if self.board.is_full():
                self.board.display()
                print('It is a draw!')
                break

            self.current_player = self.player2 if self.current_player == self.player1 else self.player1



game = Game()
game.play()