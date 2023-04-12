import pygame

eraser = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((640, 480))    
clock = pygame.time.Clock()
screen.fill((255, 255, 255))

def main():    
    radius = 15
    mode = black
    last_pos = None
    draw = "line"

    while True:
        # handle events
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and draw == "line":
                # start a new line
                last_pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION and event.buttons[0] and draw == "line":
                # draw a line from the last point to the current point
                if last_pos is not None:
                    start_pos = last_pos
                    end_pos = pygame.mouse.get_pos()
                    drawLineBetween(screen, start_pos, end_pos, radius, mode)
                    last_pos = end_pos

            if(draw == "rect" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
                drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
            if(draw == "square" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
                drawSquare(screen, pygame.mouse.get_pos(), 100, 100, mode)
            if(draw == "circle" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
                drawCircle(screen, pygame.mouse.get_pos(), mode)
            if(draw == "etrien" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
                drawRightTriangle(screen, mode, pygame.mouse.get_pos())
            if(draw == "trien" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
                drawEquilateralTriangle(screen, mode, pygame.mouse.get_pos())
            if(draw == "rhombus" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
                drawRhombus(screen, mode, pygame.mouse.get_pos())

            if(0 <= mouseY <= 30):
                if(10 <= mouseX <= 30):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        mode = black
                elif(30 <= mouseX <= 50):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        mode = green
                elif(50 <= mouseX <= 70):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        mode = blue
                elif(70 <= mouseX <= 90):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        mode = yellow
                elif(90 <= mouseX <= 110):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        mode = red
                elif(600 <= mouseX <= 630):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        mode = eraser
                elif(150 <= mouseX <= 170):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        draw = "line"
                elif(170 <= mouseX <= 200):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        draw = "rect"
                elif(200 <= mouseX <= 230):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        draw = "square"
                elif(230 <= mouseX <= 255):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        draw = "circle"
                elif(255 <= mouseX <= 285):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        draw = "etrien"
                elif(285 <= mouseX <= 315):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        draw = "trien"
                elif(315 <= mouseX <= 345):
                    if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                        draw = "rhombus"

        taskBar()

        pygame.display.flip()
        clock.tick(60)
        

def drawLineBetween(screen, start, end, width, color_mode):
    
    color = color_mode
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3) # 4th parameter is outline of the rectangle

def drawCircle(screen, mouse_pos, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.circle(screen, color, (x, y), 100, 3) # 4th parameter is outline of the rectangle

def drawSquare(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3) # 4th parameter is outline of the square

def drawRightTriangle(screen, color, mouse_pos):
    #define the points in a uint space
    x = mouse_pos[0]
    y = mouse_pos[1]
    triangle_size = 50

    # Calculate the triangle's vertices
    triangle_points = [
        (x, y - triangle_size),
        (x - triangle_size, y + triangle_size),
        (x + triangle_size, y + triangle_size),
    ]

    # Draw the triangle
    pygame.draw.polygon(screen, color, triangle_points)

def drawEquilateralTriangle(screen, color, mouse_pos):
    #define the points in a uint space
    x = mouse_pos[0]
    y = mouse_pos[1]
    triangle_size = 50

    # Calculate the triangle's vertices
    triangle_points = [
        (x, y - triangle_size - 100),
        (x - triangle_size, y + triangle_size),
        (x + triangle_size, y + triangle_size),
    ]

    # Draw the triangle
    pygame.draw.polygon(screen, color, triangle_points)  

def drawRhombus(screen, color, mouse_pos):
    #define the points in a uint space
    x = mouse_pos[0]
    y = mouse_pos[1]
    rhombus_height = 50
    rhombus_width = 50

    # Calculate the rhombus's vertices
    rhombus_points = [
        (x, y - rhombus_height),
        (x + rhombus_width, y),
        (x, y + rhombus_height),
        (x - rhombus_width , y),
    ]

    # Draw the triangle
    pygame.draw.polygon(screen, color, rhombus_points)

# Drawing taskbar  
def taskBar():
    menu = pygame.image.load("menu.png")
    screen.blit(menu, (0, 0))
    
    black_rect = (10, 5, 20, 20)
    pygame.draw.rect(screen, black, black_rect)
    green_rect = (30, 5, 20, 20)
    pygame.draw.rect(screen, green, green_rect)
    blue_rect = (50, 5, 20, 20)
    pygame.draw.rect(screen, blue, blue_rect)
    yellow_rect = (70, 5, 20, 20)
    pygame.draw.rect(screen, yellow, yellow_rect)
    red_rect = (90, 5, 20, 20)
    pygame.draw.rect(screen, red, red_rect)

    lineImage = pygame.image.load("drawline.png")
    lineImage = pygame.transform.scale(lineImage, (20, 20))
    screen.blit(lineImage, (150, 5))

    rectImage = pygame.image.load("rect.png")
    rectImage = pygame.transform.scale(rectImage, (30, 30))
    screen.blit(rectImage, (170, 0))

    squareImage = pygame.image.load("square.png")
    squareImage = pygame.transform.scale(squareImage, (30, 30))
    screen.blit(squareImage, (200, 0))

    circleImage = pygame.image.load("circle.png")
    circleImage = pygame.transform.scale(circleImage, (25, 25))
    screen.blit(circleImage, (230, 3))

    etrienImage = pygame.image.load("etrien.png")
    etrienImage = pygame.transform.scale(etrienImage, (30, 30))
    screen.blit(etrienImage, (255, 0))

    trienImage = pygame.image.load("trien.png")
    trienImage = pygame.transform.scale(trienImage, (30, 30))
    screen.blit(trienImage, (285, 0))

    rhombusImage = pygame.image.load("rhombus.png")
    rhombusImage = pygame.transform.scale(rhombusImage, (30, 30))
    screen.blit(rhombusImage, (315, 0))

    eraserImage = pygame.image.load("eraser.png")
    eraserImage = pygame.transform.scale(eraserImage, (30, 30))
    screen.blit(eraserImage, (600, 0))
main()