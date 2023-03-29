import pygame
from pygame import mixer
# import time
import datetime

#black - minute, blue - hour, red - second

pygame.init()
mixer.init()


screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
FPS = 50
done = False
myClock = pygame.image.load('image.png')
myClock = pygame.transform.scale(myClock, (600, 600))


hour_arrow = pygame.image.load('hour.png')
hour_arrow = pygame.transform.scale(hour_arrow, (35 // 1.5, 250 // 1.5))
minute_arrow = pygame.image.load('minute.png') # 30:257
minute_arrow = pygame.transform.scale(minute_arrow, (30 // 1.5, 350 // 1.5))
second_arrow = pygame.image.load('second.png')
second_arrow = pygame.transform.scale(second_arrow, (25 // 1.5, 400 // 1.5))


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        # angleSECOND -= 1
        my_time = datetime.datetime.now()
        hourINT = int(my_time.strftime("%I"))
        minuteINT = int(my_time.strftime("%M"))
        secondINT = int(my_time.strftime("%S"))

        angleHOUR = hourINT * 30 * -1
        angleMINUTE = minuteINT * 6 * -1
        angleSECOND = secondINT * 6 * -1

        hour = pygame.transform.rotate(hour_arrow, angleHOUR)
        minute = pygame.transform.rotate(minute_arrow, angleMINUTE)
        second = pygame.transform.rotate(second_arrow, angleSECOND)
        
        # second = pygame.transform.scale(second, (20, 173))

        screen.fill((255, 255, 255))
        screen.blit(myClock, (100, 100))
        screen.blit(second, (399 - int(second.get_width() / 2), 400 - int(second.get_height() / 2)))
        screen.blit(hour, ((399 - int(hour.get_width() / 2), 400 - int(hour.get_height() / 2))))
        screen.blit(minute, ((399 - int(minute.get_width() / 2), 400 - int(minute.get_height() / 2))))
        pygame.draw.circle(screen, (0, 0, 0), (400, 400), 22)
        pygame.display.flip()
        clock.tick(FPS)
        # time.sleep(1)
pygame.quit()