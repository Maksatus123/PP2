import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
done = False
clock = pygame.time.Clock()
x = 30
y = 30
screenWidth, screenHeight = screen.get_width(), screen.get_height()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - 50 > 0:
        x -= 20
    if keys[pygame.K_RIGHT] and x + 50 < screenWidth:
        x += 20
    if keys[pygame.K_UP] and y - 50 > 0:
        y -= 20
    if keys[pygame.K_DOWN] and y + 50 < screenHeight:
        y += 20
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25, 0)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()