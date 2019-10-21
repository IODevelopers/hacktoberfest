import random


class TicTacToe:
    def __init__(self, playerX, playerO):
        self.board = [' '] * 9
        self.playerX, self.playerO = playerX, playerO
        self.playerX_turn = True

    def display_board(self):
        print ('     |     |     ')
        print ('  %s  |  %s  |  %s  ' % (self.board[0],
                                        self.board[1],
                                        self.board[2]))
        print ('_____|_____|_____')
        print ('     |     |     ')
        print ('  %s  |  %s  |  %s  ' % (self.board[3],
                                        self.board[4],
                                        self.board[5]))
        print ('_____|_____|_____')
        print ('     |     |     ')
        print ('  %s  |  %s  |  %s  ' % (self.board[6],
                                        self.board[7],
                                        self.board[8]))
        print ('     |     |     ')

    def board_full(self):
        return not any([space == ' ' for space in self.board])

    def player_wins(self, char):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if char == self.board[a] == self.board[b] == self.board[c]:
                return True

        return False

    def play_game(self):
        print ('\nNew game!')

        while True:
            if self.playerX_turn:
                player, char = self.playerX, 'X'
            else:
                player, char = self.playerO, 'O'

            if player.breed == 'human':
                self.display_board()

            move = player.move(self.board)
            self.board[move - 1] = char

            if self.player_wins(char):
                self.display_board()
                print (char + ' wins!')
                break

            if self.board_full():
                self.display_board()
                print ('Draw!')
                break

            self.playerX_turn = not self.playerX_turn


class Player(object):
    def __init__(self):
        self.breed = 'human'

    def move(self, board):
        return int(input('Your move? '))

    def available_moves(self, board):
        return [i + 1 for i in range(0, 9) if board[i] == ' ']


class MinimaxPlayer(Player):
    def __init__(self):
        self.breed = 'minimax'

    def move(self, board):
        if len(self.available_moves(board)) == 9:
            return random.choice([1, 3, 7, 9])

        best_value = 0
        for move in self.available_moves(board):
            board[move - 1] = 'X'
            value = self.min_value(board)
            board[move - 1] = ' '
            if value > best_value:
                return move

        return random.choice(self.available_moves(board))

    def terminal_test(self, board):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]:
            if 'X' == board[a] == board[b] == board[c]:
                return (True, 1)
            elif 'O' == board[a] == board[b] == board[c]:
                return (True, -1)

        if not any([space == ' ' for space in board]):
            return (True, 0)

        return (False, 0)

    def max_value(self, board):
        in_terminal_state, utility_value = self.terminal_test(board)
        if in_terminal_state:
            return utility_value

        value = -100000
        for move in self.available_moves(board):
            board[move - 1] = 'X'
            value = max(value, self.min_value(board))
            board[move - 1] = ' '

        return value

    def min_value(self, board):
        in_terminal_state, utility_value = self.terminal_test(board)
        if in_terminal_state:
            return utility_value

        value = 100000
        for move in self.available_moves(board):
            board[move - 1] = 'O'
            value = min(value, self.max_value(board))
            board[move - 1] = ' '

        return value


p1 = MinimaxPlayer()
p2 = Player()

while True:
    t = TicTacToe(p1, p2)
    t.play_game()
