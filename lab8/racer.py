# Imports
# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing
pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("racer_assets/coin.png"), (40, 40))
        self.rect = self.image.get_rect()

    def generateCoin(self, enemy_pos):
        enemy_rect_pos = [j for j in range(enemy_pos[0] - 50, enemy_pos[0] + 50)]
        self.rect.center = (random.choice([i for i in range(40, SCREEN_WIDTH - 40) if i not in enemy_rect_pos]), 0)

    def move(self, enemy_pos, SPEED):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.generateCoin(enemy_pos)

    def hasCollided(self, enemy_pos):
        self.generateCoin(enemy_pos)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer_assets/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.center = self.rect.center

    def move(self, SPEED, onSuccess):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.center = self.rect.center
            onSuccess()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer_assets/Player.png")
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


class Game:
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    FPS = 60

    def __init__(self):
        self.SPEED = 5
        self.enemies_passed = 0
        self.coins_collected = 0

        # Set up Default Values
        self.enemies = None
        self.neutral = None
        self.coins = None
        self.DISPLAYSURF = None
        self.player = None
        self.enemy = None

    def setUpGameObjects(self):
        # Setting up Sprites
        self.player = Player()
        self.enemy = Enemy()
        coin = Coin()

        # Creating Sprites Groups
        self.enemies = pygame.sprite.Group()
        self.enemies.add(self.enemy)
        self.neutral = pygame.sprite.Group()
        self.neutral.add(self.player)
        self.coins = pygame.sprite.Group()
        self.coins.add(coin)

    # used for incrementing score for cars
    def enemyHasPassed(self):
        self.enemies_passed += 1

    # used for incrementing score for collected coins
    def collectCoin(self):
        self.coins_collected += 1

    def run(self):
        # Create a white screen
        self.DISPLAYSURF = pygame.display.set_mode((400, 600))
        self.DISPLAYSURF.fill(self.WHITE)
        pygame.display.set_caption("Game")

        # Adding a new User event
        INC_SPEED = pygame.USEREVENT + 1
        pygame.time.set_timer(INC_SPEED, 1000)

        # Setting up Fonts
        font = pygame.font.SysFont("Verdana", 60)
        font_small = pygame.font.SysFont("Verdana", 20)
        game_over = font.render("Game Over", True, self.BLACK)

        # road
        background = pygame.image.load("racer_assets/AnimatedStreet.png")

        # Setting up FPS
        FramePerSec = pygame.time.Clock()

        # Game Loop
        while True:

            # Cycles through all events occurring
            for event in pygame.event.get():
                if event.type == INC_SPEED:
                    self.SPEED += 0.5
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.DISPLAYSURF.blit(background, (0, 0))
            enemies_passed = font_small.render(f"Cars: {self.enemies_passed}", True, self.BLACK)
            self.DISPLAYSURF.blit(enemies_passed, (10, 10))

            coins_collected = font_small.render(f"Coins: {self.coins_collected}", True, self.BLACK)
            self.DISPLAYSURF.blit(coins_collected, (SCREEN_WIDTH - 100, 10))

            # Moves and Re-draws all Sprites
            for e in self.enemies:
                self.DISPLAYSURF.blit(e.image, e.rect)
                e.move(self.SPEED, lambda: self.enemyHasPassed())

            for n in self.neutral:
                self.DISPLAYSURF.blit(n.image, n.rect)
                n.move()

            for c in self.coins:
                self.DISPLAYSURF.blit(c.image, c.rect)
                c.move(self.enemy.center, self.SPEED)

            # To be run if collision occurs between Player and Enemy
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                pygame.mixer.Sound('racer_assets/crash.wav').play()
                time.sleep(0.5)

                self.DISPLAYSURF.fill(self.RED)
                self.DISPLAYSURF.blit(game_over, (30, 250))

                pygame.display.update()
                for entity in self.neutral:
                    entity.kill()
                time.sleep(2)
                pygame.quit()
                sys.exit()
            # To be run if collision occurs between Player and Coin
            if pygame.sprite.spritecollideany(self.player, self.coins):
                self.collectCoin()
                for c in self.coins:
                    c.hasCollided(self.enemy.center)

            pygame.display.update()
            FramePerSec.tick(self.FPS)

    def start(self):
        self.setUpGameObjects()
        self.run()


game = Game()
game.start()
