import math
from board import Board


class Player:

    def __init__(self, depthLimit, isPlayerOne):

        self.isPlayerOne = isPlayerOne
        self.depthLimit = depthLimit

    # Returns a heuristic for the board position
    # Good positions for 0 pieces are positive and good positions for 1 pieces
    # are be negative
    def heuristic(self, board):
        heur = 0
        state = board.board
        for i in range(0, board.WIDTH):
            for j in range(0, board.HEIGHT):
                # check horizontal streaks
                try:
                    # add player one streak scores to heur
                    if state[i][j] == state[i + 1][j] == 0:
                        heur += 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == 0:
                        heur += 100
                    if state[i][j] == state[i + 1][j] == state[i + 3][j] == 0:
                        heur += 100
                    if state[i][j] == state[i + 2][j] == state[i + 3][j] == 0:
                        heur += 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == 0:
                        heur += 10000
                except IndexError:
                    pass


                try:
                    # subtract player two streak score to heur
                    if state[i][j] == state[i + 1][j] == 1:
                        heur -= 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == 1:
                        heur -= 100
                    if state[i][j] == state[i + 1][j] == state[i + 3][j] == 1:
                        heur -= 100
                    if state[i][j] == state[i + 2][j] == state[i + 3][j] == 1:
                        heur -= 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == 1:
                        heur -= 10000
                except IndexError:
                    pass

                # check vertical streaks
                try:
                    # add player one vertical streaks to heur
                    if state[i][j] == state[i][j + 1] == 0:
                        heur += 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == 0:
                        heur += 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == 0:
                        heur += 10000
                except IndexError:
                    pass

                try:
                    # subtract player two streaks from heur
                    if state[i][j] == state[i][j + 1] == 1:
                        heur -= 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == 1:
                        heur -= 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == 1:
                        heur -= 10000
                except IndexError:
                    pass

                # check positive diagonal streaks
                try:
                    # add player one streaks to heur
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == 0:
                        heur += 10
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 0:
                        heur += 100
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] \
                            == state[i+3][j + 3] == 0:
                        heur += 10000
                except IndexError:
                    pass

                try:
                    # add player two streaks to heur
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == 1:
                        heur -= 10
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 1:
                        heur -= 100
                    if not j + 3 > board.HEIGHT and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] \
                            == state[i+3][j + 3] == 1:
                        heur -= 10000
                except IndexError:
                    pass

                # check negative diagonal streaks
                try:
                    # add  player one streaks
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == 0:
                        heur += 10
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == 0:
                        heur += 100
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                            == state[i+3][j - 3] == 0:
                        heur += 10000
                except IndexError:
                    pass

                try:
                    # subtract player two streaks
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == 1:
                        heur -= 10
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == 1:
                        heur -= 100
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                            == state[i+3][j - 3] == 1:
                        heur -= 10000
                except IndexError:
                    pass
        return heur


class PlayerMM(Player):
    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # returns the optimal column to move in by implementing the MiniMax algorithm
    def findMove(self, board):
        #return self.mmH(board, self.depthLimit, self.isPlayerOne)
        #return self.minMaxHelper(board, self.depthLimit, self.isPlayerOne)
        score, move = self.miniMax(board, self.depthLimit, self.isPlayerOne)
        print(self.isPlayerOne, "move made", move)
        return move

    # findMove helper function using miniMax algorithm
    def miniMax(self, board, depth, player):
        if board.isTerminal() == 0:
            return -math.inf if player else math.inf, -1
        elif depth == 0:
            return self.heuristic(board), -1

        if player:
            bestScore = -math.inf
            shouldReplace = lambda x: x > bestScore
        else:
            bestScore = math.inf
            shouldReplace = lambda x: x < bestScore

        bestMove = -1

        children = board.children()
        for child in children:
            move, childboard = child
            temp = self.miniMax(childboard, depth-1, not player)[0]
            if shouldReplace(temp):
                bestScore = temp
                bestMove = move
        return bestScore, bestMove


class PlayerAB(Player):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    # returns the optimal column to move in by implementing the Alpha-Beta algorithm
    def findMove(self, board):
        candidate = []
        score, move, candidate = self.alphaBeta(board, self.depthLimit, self.isPlayerOne, -math.inf, math.inf, candidate)
        return move, candidate

    # findMove helper function, utilizing alpha-beta pruning within the  minimax algorithm
    def alphaBeta(self, board, depth, player, alpha, beta, candidate):
        if board.isTerminal() == 0:
            return -math.inf if player else math.inf, -1
        elif depth == 0:
            return self.heuristic(board), -1

        if player:
            bestScore = -math.inf
            shouldReplace = lambda x: x > bestScore
        else:
            bestScore = math.inf
            shouldReplace = lambda x: x < bestScore

        bestMove = -1

        children = board.children()
        for child in children:
            move, childboard = child
            temp = self.alphaBeta(childboard, depth-1, not player, alpha, beta, candidate)[0]

            if depth == self.depthLimit:
                print(str(move+1) + "열 선택 시: " + str(temp))
                candidate.append(str(temp))

            if shouldReplace(temp):
                bestScore = temp
                bestMove = move
            if player:
                alpha = max(alpha, temp)
            else:
                beta = min(beta, temp)
            if alpha >= beta:
                break
        return bestScore, bestMove, candidate


class ManualPlayer(Player):
    def findMove(self, board):
        opts = " "
        for c in range(board.WIDTH):
            opts += " " + (str(c + 1) if len(board.board[c]) < 6 else ' ') + "  "
        print(opts)

        while True:
            col = input(('O' if self.isPlayerOne else 'X') + " 말을 놓을 열을 선택하세요: ")
            try:
                col = int(col) - 1
                if col < board.WIDTH and len(board.board[col]) < 6:
                    break
            except ValueError:
                pass

            print("선택할 수 없는 열입니다. 다시 선택하세요.\n")

        return col
