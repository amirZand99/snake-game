import pygame
import time
import random

pygame.init()
dis_width = 800
dis_height = 900

screen = pygame.display.set_mode((dis_width, dis_height))
image = pygame.image.load('/home/amir/Downloads/_400b86d6-92a7-40f4-b294-470887be9914.jpeg')
pygame.display.set_caption('Snake game by amirZand99')

game_over = False
paused = False

x1 = 400
y1 = 450


x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

blue = (0, 0, 255)
red = (255, 0, 0)
gold = (253, 240, 13)
green = (31, 153, 12)
black = (0, 0, 0)

snake_block = 15

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 45)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    screen.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        if i == 0:  # Draw the head with a different color
            pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])
        else:  # Draw the body segments with the regular color
            pygame.draw.rect(screen, blue, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    msg = font_style.render(msg, True, color)
    screen.blit(msg, [dis_width / 2 - 100 , dis_height / 2])

def gameLoop():  # creating a function
    global paused
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.blit(image, (0, 0))
            message("You Lost! Press esc", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = False
                        game_close = False
                    if event.key == pygame.K_ESCAPE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    paused = not paused  # Toggle pause with Space key
                    if paused:
                        x1_change = 0
                        y1_change = 0

                elif event.key == pygame.K_LEFT and not paused:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and not paused:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and not paused:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and not paused:
                    y1_change = snake_block
                    x1_change = 0

        # screen.blit(image, (0, 0))
        # x1 += x1_change
        # y1 += y1_change

        # Check if snake hits the boundaries
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.blit(image, (0, 0))
        pygame.draw.rect(screen, gold, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        if (foodx <= x1 <= foodx + snake_block or x1 <= foodx <= x1 + snake_block) and \
                (foody <= y1 <= foody + snake_block or y1 <= foody <= y1 + snake_block):
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 10.0
            Length_of_snake += 1

        clock.tick(15)

    if game_over:
        screen.blit(image, (0, 0))
        message("You lost", red)
        pygame.display.update()
        time.sleep(2)

    pygame.quit()
    quit()
gameLoop()