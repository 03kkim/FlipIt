import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Title of Window
pygame.display.set_caption("FlipIt")

# square sprite
unlitSquare = pygame.image.load('./sprites/unlitSquare.png')


def player():
    screen.blit(unlitSquare, (400 - 98, 300 - 98))

running = True
while running:

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player()
    pygame.display.update()