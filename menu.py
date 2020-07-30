import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((498, 498), 0, 32)

font = pygame.font.SysFont("Helvetica Neue", 100)

# x, y is the center of the text
def draw_text(text, font, color, x, y, surface=screen):
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=(x, y))
    surface.blit(text, text_rect)

click = False


def main_menu():
    while True:

        screen.fill((255, 255, 255))

        draw_text("FlipIt", font, (0, 0, 0), 498/2, 100)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(124, 200, 250, 76)
        button_2 = pygame.Rect(124, 300, 250, 76)
        pygame.draw.rect(screen, (128, 128, 128), button_1)
        pygame.draw.rect(screen, (128, 128, 128), button_2)

        draw_text("Play Game", pygame.font.SysFont("Helvetica Neue", 40), (150, 255, 100), 498/2, 236)
        draw_text("Options", pygame.font.SysFont("Helvetica Neue", 40), (150, 255, 255), 498 / 2, 334)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()


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
        mainClock.tick(60)


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()