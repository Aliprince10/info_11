import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

player = pygame.Rect((300, 250 ,50, 50))

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
run = True
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,(255,0,0), player)

    key = pygame.key.get_pressed()
    if key [pygame.K_w] == True:
        player.move_ip(0, -5)
    if key[pygame.K_s] == True:
        player.move_ip(0, 5)
    if key[pygame.K_d] == True:
        player.move_ip(5, 0)
    if key[pygame.K_a] == True:
        player.move_ip(-5, 0)

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False

    pygame.display.update()
pygame.quit()