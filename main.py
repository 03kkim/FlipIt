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

"""
[{0: [8, 13]}, {1: [5, 15]}, {2: [13, 1]}, {3: [2, 11]}, 
 {4: [12, 10]}, {5: [1, 12]}, {6: [15, 8]}, {7: [0, 9]}, 
 {8: [14, 3]}, {9: [6, 2]}, {10: [11, 6]}, {11: [9, 4]}, 
 {12: [10, 5]}, {13: [3, 7]}, {14: [7, 0]}, {15: [4, 14]}]


Loop #1 (7 long) {0: (8, 13)}, {2: (13, 1)}, {5: (1, 12), {4: (12, 10)}, {12: (10,5)}, {1: (5, 15)}, {6: (15,8)} 
Loop #2 (3 long) {3: (2, 11)}, {10: (11, 6)}, {9: (6, 2)}
Loop #3 (6 long) {7: (0, 9)}, {11: (9, 4)}, {15: (4, 14)}, {8: (14, 3)}, {13: (3, 7)}, {14: (7, 0)}

solve for 5 and 11 <== Not solvable

Notes:
- Loops should be even lengths, or else the puzzle will not be solvable
- Grid size must therefore be even, or if it is odd, one square must have a 1:odd relationship
- One way to generate the relationships would be to randomly make a list of the numbers 0-15. Transfer each of these twice to a separate list.
- To make 1 big loop, just remove the first element from that list, and move it to the end.
- To make multiple loops, split the list in between two numbers and do the same process for the big loop. (Make sure the len(list)%4 == 0)
"""



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




