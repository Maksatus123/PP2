#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COINSPEED = 5
SCORE = 0
COINS = 0
LEVEL = 1

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# creating an enemy class
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600): # if our enemy will be on the bottom of our screen it will be respawned
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# creating a player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

# creating a coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.randomCoin = random.randint(1, 3)
        self.image = pygame.image.load(f"coin{self.randomCoin}.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
        


    def move(self):
        global COINS
        self.rect.move_ip(0,COINSPEED)
        if (self.rect.bottom > 600): # if our coin will go under the screen it will be respawned
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


#Setting up Sprites        
P1 = Player()
E1 = Enemy()
COIN = Coin()
coin_dup = 0
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(COIN)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(COIN)

#Adding a new User event 
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

# level_duplicate = LEVEL
def levelAdder():
    global LEVEL
    global SPEED
    if COINS // 4 > LEVEL:
        LEVEL += 1
        SPEED += 3
        # print(SPEED)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #       SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    collected = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(collected, (400 - 30,10))
    levels = font_small.render(str(LEVEL), True, BLACK)
    DISPLAYSURF.blit(levels, (400 - 30, 400 - 30))
    

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        

    # if our player will collide with the coin object what will be:
    # the collecting sound will be played
    # the coin object will be destroyed
    if pygame.sprite.spritecollideany(P1, coins):
            pygame.mixer.Sound('collect.wav').play()
            for coin in coins:
                coin.kill()
        #   time.sleep(1)
            # randomCoin = random.randint(1, 3)
            if COIN.randomCoin == 1:
                COINS += 1
            if COIN.randomCoin == 2:
                COINS += 2
            if COIN.randomCoin == 3:
                COINS += 3
            pygame.display.update() 
    if(len(coins) == 0): # if our coin was collected:
        
        # coin spawn
        COIN = Coin()   # new coin object will be created and added to the coins group
        coins.add(COIN)
        all_sprites.add(COIN)

    levelAdder()

    pygame.display.update()
    FramePerSec.tick(FPS)
