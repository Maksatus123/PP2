import pygame 
from pygame import mixer

pygame.init()
mixer.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 50
done = False
n = 0
musics = ['music/boom.mp3', 'music/incoming.mp3', 'music/crisis.mp3', 'music/hymnfortheweekend.mp3', 'music/afterdarkxsweatherweather.mp3']
plays = ['boom.png', 'incoming.png', 'crisis.png', 'hymnfortheweekend.png', 'afterdark.png']
pause = 'pause.png'
play = 'play-buttton.png'
rewind_button = 'rewind-button.png'
forward_button = 'forward-button.png'

def start(n):
    
    # Loading nth audio file into our player
    mixer.music.load(musics[n])
      
    mixer.music.set_volume(0.2)
    # Playing our music
    mixer.music.play()

start(n)
screen.fill((255, 255, 255))
screen.blit(pygame.image.load(plays[n]), (150, 100))
screen.blit(pygame.image.load(play), (380, 650))
screen.blit(pygame.image.load(rewind_button), (350, 650))
screen.blit(pygame.image.load(forward_button), (410, 650))
paused = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if(paused == False):
                mixer.music.pause()
                paused = True
                
                screen.fill((255, 255, 255))
                screen.blit(pygame.image.load(pause), (380, 650))
                screen.blit(pygame.image.load(plays[n]), (150, 100))
                screen.blit(pygame.image.load(rewind_button), (350, 650))
                screen.blit(pygame.image.load(forward_button), (410, 650))
            else:
                mixer.music.unpause()
                paused = False
                screen.fill((255, 255, 255))
                screen.blit(pygame.image.load(plays[n]), (150, 100))
                screen.blit(pygame.image.load(play), (380, 650))
                screen.blit(pygame.image.load(rewind_button), (350, 650))
                screen.blit(pygame.image.load(forward_button), (410, 650))
            # b = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if n == 4: n = 0
            else: n += 1
            screen.fill((255, 255, 255))
            screen.blit(pygame.image.load(plays[n]), (150, 100))
            screen.blit(pygame.image.load(play), (380, 650))
            screen.blit(pygame.image.load(rewind_button), (350, 650))
            screen.blit(pygame.image.load(forward_button), (410, 650))
            start(n)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if n == 0: n = 4
            else: n -= 1
            screen.fill((255, 255, 255))
            screen.blit(pygame.image.load(plays[n]), (150, 100))
            screen.blit(pygame.image.load(play), (380, 650))
            screen.blit(pygame.image.load(rewind_button), (350, 650))
            screen.blit(pygame.image.load(forward_button), (410, 650))
            start(n)
  
    pygame.display.flip()
    clock.tick(FPS)
# start(0)
pygame.quit()