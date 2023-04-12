import pygame
from pygame.math import Vector2
import datetime
import random 


# creating a snake class 
class Snake:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)] # head, and body elements of the snake
        self.eated = False # checker for snake eated the fruit or not
        self.isDead = False # check snake dead or not

    # drawing our snake
    def drawingSnake(self):
        for block in self.body: # the for loop that iterate our list of cooredinates of snake elements
            body_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size) # creating rectangle of the snake elements
            pygame.draw.rect(screen, (0 ,128 ,0), body_rect) # drawing the rectangles

    # the moving of our snake
    def snakeMoving(self):
        if self.eated == True: # if snake eated the fruit
            body_copy = self.body[:] # take the copy of the snake
            body_copy.insert(0, body_copy[0] + direction) # adding the one element
            self.body = body_copy[:] 
            self.eated = False
        else:
            body_copy = self.body[:-1] # taking the copy of the snake except the last element
            body_copy.insert(0, body_copy[0] + direction) # adding one element at index 0 this element is our head + direction
            self.body = body_copy[:]

# creating our Fruit class
class Fruit:
    def __init__(self):
        self.randomize() # the method that spawns our fruit at the random position
    
    def drawingFruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size) 
        self.food = pygame.image.load(f'food{self.randomFood}.png').convert_alpha() # spawning random fruit
        self.food = pygame.transform.scale(self.food, (35, 35)) # scale the image
        # pygame.draw.rect(screen, (107 ,142 ,35), fruit_rect)
        screen.blit(self.food, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 2) # random cell between 0 - 18, whu 18 because if it will be bigger, the fruit will spawn on the borders 
        self.y = random.randint(0, cell_number - 2) 
        self.pos = Vector2(self.x, self.y)
        self.randomFood = random.randint(1, 3) # taking random number between 1-3

# creating the game class that will allow us to control the game
class Game:
    def __init__(self):
        self.snake = Snake() # creating the snake object
        self.fruit = Fruit() # creating the fruit object
        self.level = 1 # our 1st level
        self.snake_speed = 5 # snake speed, actually it is snake speed
        self.score = 0 # the score, that will increase after eating the fruit
        # self.isDead = False

    # update method which responsible to snake moving and collision checker
    def update(self):
        self.snake.snakeMoving()
        self.checkCollision()
        # self.levelAdding()

    def drawElements(self):
        self.snake.drawingSnake()
        self.fruit.drawingFruit()
        self.scoreDrawing()
    
    def checkCollision(self):
        if(self.fruit.pos == self.snake.body[0]): # if the coordinates of our snake and fruit will be equal, snake will eat
            self.snake.eated = True
            # the 3 types of the food that gives to us, three types of score
            if(self.fruit.randomFood == 1):
                self.score += 1
            if(self.fruit.randomFood == 2):
                self.score += 2
            if(self.fruit.randomFood == 3):
                self.score += 3
            self.fruit.randomize() # after eating spawning at the random position
            self.levelAdding() # check for adding level

    # check for our snake collides with borders
    def gameOver(self):
        if self.snake.body[0].x >= 19:
            return True
        if self.snake.body[0].x <= 0:
            return True
        if self.snake.body[0].y >= 19:
            return True
        if self.snake.body[0].y <= 0:
            return True
        
        # check for our snake collides with his body
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return True
        return False
    
    # check for adding level or not for evety 3 points
    def levelAdding(self):
        if self.score % 3 == 0:
            self.level += 1
            self.snake_speed += 1
    
    # drawing the UI of our game, such us score and level
    def scoreDrawing(self):
        score_text = "Score: " + str(self.score)
        score_surface = font.render(score_text, True, (56, 74, 12))
        score_rect = score_surface.get_rect(center = (cell_size * cell_number - 120, 40))
        screen.blit(score_surface, score_rect)

        level_text = "Level: " + str(self.level)
        level_surface = font.render(level_text, True, (56, 74, 12))
        level_rect = level_surface.get_rect(center = (cell_size * cell_number - 120, 70))
        screen.blit(level_surface, level_rect)




pygame.init()
clock = pygame.time.Clock()
cell_size = 40
cell_number = 20
direction = Vector2(1, 0) # direction this means to right
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number)) # creating screen with are 800x800 or 20x20 cells square
done = False



font = pygame.font.Font('font.ttf', 25) # imporing our font, from our file

nowSeconds = int((datetime.datetime.now()).strftime("%S"))

game = Game() # creating the game object
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # check for direction
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if direction.x != -1:
                direction = Vector2(1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if direction.x != 1:
                direction = Vector2(-1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if direction.y != 1:
                direction = Vector2(0, -1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if direction.y != -1:
                direction = Vector2(0, 1)

    if(game.gameOver() == True): # if our game over returns true, we will end the game
        done = True
    
    # check for to randomly spawn the fruit, if you wont eat the frut after 3 seconds it will be spawned at the random position
    time = datetime.datetime.now()
    seconds = int(time.strftime("%S"))
    if abs(seconds - nowSeconds) > 3:
        game.fruit.randomize()
        nowSeconds = seconds
    screen.fill((175, 215, 70))
    game.drawElements()
    game.update()
    pygame.display.flip()
    clock.tick(game.snake_speed)
pygame.quit()
