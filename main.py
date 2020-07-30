import pygame, sys
from board import Board

pygame.init()

# Set the width and height of the screen [width, height]
global size
size = (498, 620)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Used for Text Display
font = pygame.font.SysFont("Helvetica Neue", 100)

# x, y is the center of the text
def draw_text(text, font, color, x, y, surface=screen):
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=(x, y))
    surface.blit(text, text_rect)



# Used to manage how fast the screen updates
clock = pygame.time.Clock()



def game():
    # Sets up board
    board = Board()
    board.create_relationships()
    print(board.relationships)
    grid = board.return_grid()
    object_grid = []

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = ((128, 128, 128))
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    highlight1 = RED
    highlight2 = GREEN

    # Variables for individual squares
    width = 112
    height = 112
    margin = 10

    offset = size[1] - 498

    # Used in loop
    done = False
    last_highlighted = []

    # Stopwatch Setup
    minutes = 0
    seconds = 0
    frames = 0
    oldsecond = 0

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
                row = (pos[1] - offset) // (width + margin)
                # Set that location to one
                board.switch(board.coords_to_id(row, column))
                print("Click ", pos, "Grid coordinates: ", row, column)
                grid = board.return_grid()


        # --- Game logic should go here
        for square in object_grid:
            if square.collidepoint(pygame.mouse.get_pos()):
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (width + margin)
                row = (pos[1] - offset) // (width + margin)
                currently_highlighted = [row, column]
                if currently_highlighted != last_highlighted:
                    last_highlighted = currently_highlighted
                    board.unhighlight()
                    board.highlight(board.coords_to_id(row, column))
                    print("Highlight ", pos, "Grid coordinates: ", row, column)
                    break

                elif currently_highlighted[0] == last_highlighted[0] and currently_highlighted[1] == last_highlighted[1]:
                    break
        if (board.has_won() == True):
            print("Congratulations!")
            done = True


                    # --- Screen-clearing code goes here
        screen.fill(BLACK)


        # If you want a background image, replace this clear with blit'ing the
        # background image.


        # --- Drawing code should go here
        pygame.draw.rect(screen, GRAY, (10 + 2 * (10 + 112), 10, width * 2 + 10, height), border_radius=10)
        for row in range(4):
            for column in range(4):
                color = GRAY
                if grid[row][column] == 1:
                    color = WHITE
                rect1 = pygame.draw.rect(screen, color, (margin + column * (margin + width), (margin + row * (margin + height)) + offset, width, height))

                # Adds to the object grid used to detect mouseovers
                if len(object_grid) < 16:
                    object_grid.append(rect1)

                if board.is_highlighted[board.coords_to_id(row, column)] == 2:
                    pygame.draw.rect(screen, highlight1, (margin + column * (margin + width), (margin + row * (margin + height) + offset), width, height), 5)
                if board.is_highlighted[board.coords_to_id(row, column)] == 3:
                    pygame.draw.rect(screen, highlight2, (margin + column * (margin + width), (margin + row * (margin + height) + offset), width, height), 5)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        #Stopwatch functionality
        if (frames == 59):
            frames = 0
            if (seconds == 59):
                seconds = 0
                minutes += 1
            else:
                seconds += 1
        else:
            frames += 1

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

def main_menu():
    click = False
    while True:

        screen.fill((255, 255, 255))

        draw_text("FlipIt", font, (0, 0, 0), 498/2, 150)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(124, 300, 250, 76)
        button_2 = pygame.Rect(124, 400, 250, 76)
        pygame.draw.rect(screen, (128, 128, 128), button_1, border_radius=15)
        pygame.draw.rect(screen, (128, 128, 128), button_2, border_radius=15)

        draw_text("Play Game", pygame.font.SysFont("Helvetica Neue", 40), (150, 255, 100), 498/2, 336)
        draw_text("Options", pygame.font.SysFont("Helvetica Neue", 40), (150, 255, 255), 498 / 2, 434)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        # if button_2.collidepoint((mx, my)):
        #     if click:
        #         options()


        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

main_menu()












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




