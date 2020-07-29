"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from board import Board

# Sets up board
board = Board()
board.create_relationships()
grid = board.return_grid()
object_grid = []



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = ((128,128,128))
GREEN = (0, 255, 0)
RED = (255, 0, 0)
highlight1 = RED
highlight2 = GREEN
# Variables for individual squares
width = 112
height = 112
margin = 10

pygame.init()

# Set the width and height of the screen [width, height]
size = (498, 498)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + margin)
            row = pos[1] // (width + margin)
            # Set that location to one
            board.switch(board.coords_to_id(row, column))
            print("Click ", pos, "Grid coordinates: ", row, column)
            grid = board.return_grid()

        for square in object_grid:
            if square.collidepoint(pygame.mouse.get_pos()):
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (width + margin)
                row = pos[1] // (width + margin)
                # Set that location to one
                board.highlight(board.coords_to_id(row, column))
                print("Highlight ", pos, "Grid coordinates: ", row, column)
                grid = board.return_grid()



    screen.fill(BLACK)
    # --- Game logic should go here
    for row in range(4):

        for column in range(4):
            color = GRAY
            if grid[row][column] == 1:
                color = WHITE
            rect1 = pygame.draw.rect(screen, color, (margin + column * (margin + width), (margin + row * (margin + height)), width, height))

            # Adds to the object grid used to detect mouseovers
            if len(object_grid) < 16:
                object_grid.append(rect1)

            if board.is_highlighted[board.coords_to_id(row, column)] == 2:
                pygame.draw.rect(screen, highlight1, (margin + column * (margin + width), (margin + row * (margin + height)), width, height), 5)
            if board.is_highlighted[board.coords_to_id(row, column)] == 3:
                pygame.draw.rect(screen, highlight2, (margin + column * (margin + width), (margin + row * (margin + height)), width, height), 5)

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
























# from board import Board
# import os
#
# board = Board()
# board.create_relationships()
# print(board.relationships)
# turn = 0
# board.print_grid()
#
# while (board.has_won() == False):
#     # inp = input("Input 1 to highlight, 2 to switch, and 3 to clear the board\n")
#     # if (inp == "1"):
#     #     highlight_id = int(input("Where would you like to highlight?\n"))
#     #
#     #     board.highlight(highlight_id)
#     # else:
#     #     if (inp != "2" and inp != "3"):
#     #         print("Invalid input! Try again.")
#     #
#     #     elif (inp == "2"):
#     #         switch_id = int(input("Where would you like to switch?\n"))
#     #         board.switch(switch_id)
#     #
#     #     elif (inp == "3"):
#     #         board.clear_board()
#     switch_id = int(input(""))
#     board.switch(switch_id)
#     board.print_grid()
#
#     turn += 1
#
# print("You win!")



























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




