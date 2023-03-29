import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3
    screen.fill((0, 0, 0))

    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
    clock.tick(60)


# import pygame
# import os

# _image_library = {}
# def get_image(path):
#         global _image_library
#         image = _image_library.get(path)
#         if image == None:
#                 canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
#                 image = pygame.image.load(canonicalized_path)
#                 _image_library[path] = image
#         return image

# pygame.init()
# screen = pygame.display.set_mode((400, 300))
# done = False
# clock = pygame.time.Clock()
# surface = pygame.Surface((100, 100), pygame.SRCALPHA)

# while not done:
#         for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                         done = True
        
#         screen.fill((255, 255, 255))
        
#         screen.blit(get_image('ball.png'), (20, 20))
        
#         pygame.display.flip()
#         clock.tick(60)