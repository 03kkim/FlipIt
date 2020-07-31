import pygame, sys
from board import Board

pygame.init()

# Set the width and height of the screen [width, height]
global size
size = (498, 620)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("FlipIt")

# Used for Text Display
font = pygame.font.SysFont("Montserrat", 100)

# x, y is the center of the text
def draw_text(text, font, color, x, y, surface=screen):
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=(x, y))
    surface.blit(text, text_rect)



# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def main_menu():
    c1 = pygame.Color("#45A29E")
    c2 = pygame.Color("#66FCF1")
    c3 = pygame.Color("#C5C6C7")
    c4 = (255, 255, 255)
    c5 = pygame.Color("#0B0C10")
    click = False
    while True:

        screen.fill(c1)

        draw_text("FlipIt", font, (0, 0, 0), 498/2, 150)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(124, 300, 250, 76)
        button_2 = pygame.Rect(124, 400, 250, 76)

        pygame.draw.rect(screen, c3, button_1, border_radius=15)
        pygame.draw.rect(screen, c2, button_1, 5, border_radius=15)

        pygame.draw.rect(screen, c3, button_2, border_radius=15)
        pygame.draw.rect(screen, c2, button_2, 5, border_radius=15)

        # Was "Helvetica Neue
        draw_text("Play Game", pygame.font.SysFont("Montserrat", 40), c5, 498/2, 336)
        draw_text("Options", pygame.font.SysFont("Montserrat", 40), c5, 498 / 2, 434)

        if button_1.collidepoint((mx, my)):

            # Makes Play button white on mouseover
            pygame.draw.rect(screen, c3, button_1, border_radius=15)
            pygame.draw.rect(screen, c4, button_1, 5, border_radius=15)
            draw_text("Play Game", pygame.font.SysFont("Montserrat", 40), c5, 498 / 2, 336)
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

    # c1 is background, c2 is border color, c3 is text background (also off state), c4 is on state, c5 is text color
    c1 = pygame.Color("#45A29E")
    c2 = pygame.Color("#66FCF1")
    c3 = pygame.Color("#C5C6C7")
    c4 = WHITE
    c5 = pygame.Color("#0B0C10")

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

    # Turn Counter
    turn = 0


    # -------- Main Program Loop -----------
    while not done:
        if (board.has_won() == False):
        # Set up the stopwatch
            if (minutes < 10):
                if (seconds < 10):
                    stopwatch = str(minutes) + ":" + "0" + str(seconds)
                else:
                    stopwatch = str(minutes) + ":" + str(seconds)

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
                    real_row = (pos[1]) // (width + margin)
                    if (real_row == 0 and column == 0):
                        done = True
                        main_menu()

                    board.switch(board.coords_to_id(row, column))
                    turn += 1
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



            # --- Screen-clearing code goes here
            screen.fill(c1)


            # If you want a background image, replace this clear with blit'ing the
            # background image.


            # --- Drawing code should go here
            pygame.draw.rect(screen, c3, (10, 10, width, height), border_radius=10)
            pygame.draw.rect(screen, c2, (10, 10, width, height), 5, border_radius=10)

            back_arrow = pygame.image.load("./sprites/back_arrow.svg")
            arrow_rect = back_arrow.get_rect()
            screen.blit(back_arrow, (22, 22), arrow_rect)


            turn_font = pygame.font.SysFont("Montserrat", 80)
            if (turn>=10):
                turn_font = pygame.font.SysFont("Montserrat", 70)
            if (turn >= 100):
                turn_font = pygame.font.SysFont("Montserrat", 50)
            pygame.draw.rect(screen, c3, (10 + 10 + 112, 10, width, height), border_radius=10)
            pygame.draw.rect(screen, c2, (10 + 10 + 112, 10, width, height), 5, border_radius=10)
            draw_text(str(turn), turn_font, c5, 188, 64)

            time_font = pygame.font.SysFont("Montserrat", 80)
            if (minutes >= 10):
                time_font = pygame.font.SysFont("Montserrat", 50)
            pygame.draw.rect(screen, c3, (10 + 2 * (10 + 112), 10, width * 2 + 10, height), border_radius=10)
            pygame.draw.rect(screen, c2, (10 + 2 * (10 + 112), 10, width * 2 + 10, height), 5, border_radius=10)
            draw_text(stopwatch, time_font, c5, 371, 64)


            for row in range(4):
                for column in range(4):
                    color = c3
                    if grid[row][column] == 1:
                        color = c4
                    rect1 = pygame.draw.rect(screen, color, (margin + column * (margin + width), (margin + row * (margin + height)) + offset, width, height), border_radius=5)
                    pygame.draw.rect(screen, c2, (margin + column * (margin + width), (margin + row * (margin + height) + offset), width, height), 5, border_radius=5)

                    # Adds to the object grid used to detect mouseovers
                    if len(object_grid) < 16:
                        object_grid.append(rect1)

                    if board.is_highlighted[board.coords_to_id(row, column)] == 2:
                        pygame.draw.rect(screen, highlight1, (margin + column * (margin + width) - 5, (margin + row * (margin + height) + offset) - 5, width + 10, height + 10), 5, border_radius=10)
                    if board.is_highlighted[board.coords_to_id(row, column)] == 3:
                        pygame.draw.rect(screen, highlight2, (margin + column * (margin + width) - 5, (margin + row * (margin + height) + offset) - 5, width + 10, height + 10), 5, border_radius=10)


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

        # Win Page
        elif (board.has_won() == True):
            # Stopwatch
            if (minutes < 10):
                if (seconds < 10):
                    stopwatch = str(minutes) + ":" + "0" + str(seconds)
                else:
                    stopwatch = str(minutes) + ":" + str(seconds)
            # --- Main event loop

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if (pos[0] >= 127 and pos[0] <= 239) and (pos[1] >= 400 and pos[1] <= 512):
                        done = True
                        main_menu()
                    elif (pos[0] >= 259 and pos[0] <= 371) and (pos[1] >= 400 and pos[1] <= 512):
                        board.clear_board()
                        turn = 0
                        minutes = 0
                        seconds = 0
                        frames = 0

            screen.fill(c1)

            back_box_x = 249 - 112 - 10
            back_box_y = 400
            retry_box_x = 249 + 10
            retry_box_y = 400

            pygame.draw.rect(screen, c3, (back_box_x, back_box_y, width, height), border_radius=10)
            pygame.draw.rect(screen, c2, (back_box_x, back_box_y, width, height), 5, border_radius=10)
            back_arrow = pygame.image.load("./sprites/back_arrow.svg")
            back_rect = back_arrow.get_rect()
            screen.blit(back_arrow, (back_box_x + 12, back_box_y + 12), back_rect)

            pygame.draw.rect(screen, c3, (retry_box_x, retry_box_y, width, height), border_radius=10)
            pygame.draw.rect(screen, c2, (retry_box_x, retry_box_y, width, height), 5, border_radius=10)
            retry_arrow = pygame.image.load("./sprites/retry.svg")
            retry_rect = retry_arrow.get_rect()
            screen.blit(retry_arrow, (retry_box_x + 12, retry_box_y + 12), retry_rect)

            win_font = pygame.font.SysFont("Montserrat", 50)
            draw_text("Congratulations!", win_font, c5, 249, 100)
            draw_text("Turns: " + str(turn), win_font, c5, 249, 225)
            draw_text("Time: " + stopwatch, win_font, c5, 249, 300)


        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

main_menu()