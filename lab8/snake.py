import pygame
import random
import os
from pygame.math import Vector2

pygame.init()
cell_size = 30
cell_num = 20


class Direction:
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)


class GameObject:
    def draw(self, where: pygame.Surface):
        pass

    def move(self):
        pass

    def get_pos(self) -> tuple[float, float]:
        pass


class Snake(GameObject):
    def __init__(self):
        # head of the snake is at body[0]
        self.body = [Vector2(6, 5), Vector2(5, 5), Vector2(4, 5)]
        self.direction = Direction.RIGHT

    def draw(self, where):
        for idx, block in enumerate(self.body):
            if idx == 0:
                rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                pygame.draw.rect(where, (39, 145, 10), rect)
            else:
                rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                pygame.draw.rect(where, (36, 92, 20), rect)

    def move(self):
        copy = self.body[:-1]
        copy.insert(0, self.body[0] + self.direction)  # first block of body becomes head, move head
        self.body = copy

    def get_pos(self) -> tuple[float, float]:
        return self.body[0].x, self.body[0].y

    def extend(self):
        copy = self.body[:]
        copy.insert(0, self.body[0] + self.direction)  # first block of body becomes head, move head
        self.body = copy


class Apple(GameObject):

    def __init__(self):
        self.position = Vector2(random.randint(1, cell_num - 3), random.randint(1, cell_num - 3))
        self.image = pygame.transform.scale(pygame.image.load(os.path.abspath(
            "snake_assets/apple.png")).convert_alpha(),
                                            (cell_size, cell_size))

    def draw(self, where):
        rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        where.blit(self.image, rect)

    def move(self):
        self.position = Vector2(random.randint(1, cell_num - 2), random.randint(1, cell_num - 2))

    def get_pos(self) -> tuple[float, float]:
        return self.position.x, self.position.y


class PlayBoard:
    def __init__(self, ):
        self.cell_num = cell_num
        self.cell_size = cell_size


class Game:

    def __init__(self, playb: PlayBoard):
        self.playb = playb
        self.SIZE = (playb.cell_num * playb.cell_size, playb.cell_num * playb.cell_size)
        self.running = True
        self.gameOver = False
        self.screen = pygame.display.set_mode(self.SIZE)
        self.FPS = 60
        self.TICK = 125
        self.collectedPoints = 0
        self.currLevel = 1
        self.font = pygame.font.SysFont("Arial", 16)
        self.apple = Apple()
        self.snake = Snake()

    def setScreenColor(self):
        self.screen.fill((109, 181, 83))

    def checkForFail(self):
        head = self.snake.get_pos()
        # check for the wall
        if not (0 <= head[0] < self.playb.cell_num):
            self.gameOver = True
        if not (0 <= head[1] < self.playb.cell_num):
            self.gameOver = True

        # check if we hit outselves
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameOver = True

    def renderGameInfo(self):
        level = self.font.render(f"Level {self.currLevel}", True, (0, 0, 0))
        score = self.font.render(f"Score {self.collectedPoints}", True, (0, 0, 0))
        self.screen.blit(level, ((self.playb.cell_num - 2) * self.playb.cell_size, 20.0))
        self.screen.blit(score, ((self.playb.cell_num - 2) * self.playb.cell_size, 40.0))

    def increaseLevel(self):
        self.currLevel += 1
        if self.TICK > 40:
            self.TICK -= 20

    def checkForCollision(self, MOVEMENT):
        headC = self.snake.get_pos()
        appleC = self.apple.get_pos()
        if appleC == headC:
            self.apple.move()
            self.snake.extend()
            self.collectedPoints += 1

            if self.collectedPoints >= 3 and self.collectedPoints % 3 == 0:
                self.increaseLevel()
                pygame.time.set_timer(MOVEMENT, self.TICK)

    def updateScreen(self, user_event):
        self.setScreenColor()
        self.apple.draw(self.screen)
        self.snake.draw(self.screen)
        self.checkForCollision(user_event)
        self.checkForFail()
        self.renderGameInfo()
        pygame.display.flip()

    def restart(self):
        self.apple = Apple()
        self.snake = Snake()
        self.currLevel = 1
        self.FPS = 8
        self.collectedPoints = 0
        self.updateScreen()
        self.gameOver = False

    def drawPlayBtn(self):
        restartImg = pygame.image.load(os.path.abspath("snake_assets/restart.png")).convert_alpha()
        restartImg = pygame.transform.scale(restartImg, (100, 100))
        restartBtn = self.screen.blit(restartImg,
                                      ((self.screen.get_width() / 2 - 50), (self.screen.get_height() / 2 - 50)))
        pygame.display.flip()
        return restartBtn

    def startTheApp(self):
        restartBtn = None
        MOVEMENT = pygame.USEREVENT
        pygame.time.set_timer(MOVEMENT, self.TICK)

        while self.running:
            pygame.time.Clock().tick(self.FPS)

            if not self.gameOver:
                self.updateScreen(MOVEMENT)
            else:
                restartBtn = self.drawPlayBtn()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == MOVEMENT:
                    self.snake.move()

                # update movement
                if event.type == pygame.KEYDOWN and not self.gameOver:
                    if event.key == pygame.K_UP and self.snake.direction is not Direction.DOWN:
                        self.snake.direction = Direction.UP
                    if event.key == pygame.K_DOWN and self.snake.direction is not Direction.UP:
                        self.snake.direction = Direction.DOWN
                    if event.key == pygame.K_LEFT and self.snake.direction is not Direction.RIGHT:
                        self.snake.direction = Direction.LEFT
                    if event.key == pygame.K_RIGHT and self.snake.direction is not Direction.LEFT:
                        self.snake.direction = Direction.RIGHT
                # restart the game
                if event.type == pygame.MOUSEBUTTONUP and self.gameOver and restartBtn is not None:
                    pos = pygame.mouse.get_pos()
                    if restartBtn.collidepoint(pos):
                        self.restart()


pb = PlayBoard()
snakeGame = Game(pb)
snakeGame.startTheApp()
