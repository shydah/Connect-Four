import time
from board import Board
from player import PlayerMM, PlayerAB, ManualPlayer

class Game:
    def __init__(self, startBoard, player1, player2):
        self.startBoard = startBoard
        self.player1 = player1
        self.player2 = player2

    ########################################################################
    #                     Simulate a Local Game
    ########################################################################

    def simulateLocalGame(self, isPlayer1=False):
        board = Board(orig=self.startBoard)
        turns = 0

        while(True):
            turns = turns + 1

            # finds the move to make
            start_time = time.time()
            if isPlayer1:
                move = self.player1.findMove(board)
            else:
                while True:
                    move = self.player2.findMove(board)
                    if turns == 1 and move == 3:
                        print("4열에 첫 수를 둘 수 없습니다.\n")
                    else:
                        break

            end_time = time.time()

            # makes the move
            board.makeMove(move)
            board.print()
            print(end_time - start_time)

            # determines if the game is over or not
            isOver = board.isTerminal()
            if isOver == 0:
                print("It is a draw!")
                break
            elif isOver == 1:
                print("Player 1 wins!")
                break
            elif isOver == 2:
                print("Player 2 wins!")
                break
            else:
                isPlayer1 = not isPlayer1


if __name__ == "__main__":
    while True:
        player_select = input("선공을 하시겠습니까? [Y/n]\n")
        if player_select == "Y":
            isPlayer1 = False
            break
        elif player_select == "n":
            isPlayer1 = True
            break
        else:
            print("\n올바르지 않은 입력입니다.")

    game = Game(Board(), PlayerAB(8, isPlayer1), ManualPlayer(5, True))
    game.simulateLocalGame(isPlayer1)
