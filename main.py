from board import Board

board = Board()
board.create_relationships()
# print(board.relationships)
# board.highlight(0)
# board.print_grid(board.id_states)

# while (board.has_won() == False):
#     board.unhighlight()
#     board.print_grid()
#     print(board.id_states)
#     inp = input("Input 1 to highlight, 2 to switch, and 3 to clear the board\n")
#     if (inp == "1"):
#         highlight_id = int(input("Where would you like to highlight?"))
#         board.highlight(highlight_id)
#
#     if (inp == "2"):
#         switch_id = int(input("Where would you like to switch?"))
#         board.switch(switch_id)
#
#     if (inp == "3"):
#         board.clear_board()


print(board.view_board)
print(str(board.id_states) + "\n")

board.highlight(1)
print(board.view_board)
print(str(board.id_states) + "\n")

board.unhighlight()
print(board.view_board)
print(str(board.id_states) + "\n")

board.highlight(1)
print(board.view_board)
print(str(board.id_states) + "\n")



























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




