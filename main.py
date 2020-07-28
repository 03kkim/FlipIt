from board import Board
import os

board = Board()
board.create_relationships()
print(board.relationships)
turn = 0
board.print_grid()

while (board.has_won() == False):
    # inp = input("Input 1 to highlight, 2 to switch, and 3 to clear the board\n")
    # if (inp == "1"):
    #     highlight_id = int(input("Where would you like to highlight?\n"))
    #
    #     board.highlight(highlight_id)
    # else:
    #     if (inp != "2" and inp != "3"):
    #         print("Invalid input! Try again.")
    #
    #     elif (inp == "2"):
    #         switch_id = int(input("Where would you like to switch?\n"))
    #         board.switch(switch_id)
    #
    #     elif (inp == "3"):
    #         board.clear_board()
    switch_id = int(input(""))
    board.switch(switch_id)
    board.print_grid()

    turn += 1

print("You win!")




# print(board.view_board)
# print(str(board.id_states) + "\n")
#
# board.switch(0)
# print(board.view_board)
# print(str(board.id_states) + "\n")
#
# print(board.view_board)
# print(str(board.id_states) + "\n")
#
# board.highlight(0, style="line")
# print(str(board.id_states) + "\n")



























# def draw_board(board):
    # row1 = []
    # row2 = []
    # row3 = []
    # row4 = []
    # for id in board:
    #     if (id//4 == 0):
    #         row1.append(id)
    #     if (id//4 == 1):
    #         row2.append(id)
    #     if (id//4 == 2):
    #         row3.append(id)
    #     if (id//4 == 3):
    #         row4.append(id)
    # view_board = [row1, row2, row3, row4]
    # print(row1)
    # print(row2)
    # print(row3)
    # print(row4)



# def create_relationships(board):




