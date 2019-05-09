import time
from board import Board
from player import PlayerAB, ManualPlayer


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
                move, candidate = self.player1.findMove(board)
                if turns == 1 and move == 3:
                    print("\n4열에 첫 수를 둘 수 없습니다.")
                    for index in range(len(candidate)):
                        if candidate[3] == candidate[index] and index != 3:
                            move = index
                            print(str(index+1) + "열을 대신 택하였습니다.")
                            break
                if turns % 2 == 1:
                    reason = "크기"
                    # if AI takes turn first
                else:
                    reason = "작기"
                    # if human takes turn first
                print(str(move+1) + "열에 수를 둔 이유는 해당 열의 Heuristic 값이 제일 " + reason + " 때문입니다.")
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
            print("소요 시간 : " + str(end_time - start_time) + "\n")

            if not isPlayer1:
                print("----- 상대편이 수를 두는 중입니다 ----- \n")

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

            print("\n----- 상대편이 수를 두는 중입니다 ----- \n")

            break
        else:
            print("\n올바르지 않은 입력입니다.")

    game = Game(Board(), PlayerAB(8, isPlayer1), ManualPlayer(5, True))
    game.simulateLocalGame(isPlayer1)
