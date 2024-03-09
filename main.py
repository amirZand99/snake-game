import pygame
import time

pygame.init()
dis_width = 800
dis_height = 900

screen = pygame.display.set_mode((dis_width, dis_height))
image = pygame.image.load('/home/amir/Downloads/_400b86d6-92a7-40f4-b294-470887be9914.jpeg')
pygame.display.set_caption('Snake game by amir')

game_over = False
paused = False

x1 = 400
y1 = 450

snake_block = 10

font_style = pygame.font.SysFont(None, 90)


def message(msg, color):
    msg = font_style.render(msg, True, color)
    screen.blit(msg, [dis_width / 2 - 100 , dis_height / 2])


x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

blue = (0, 0, 255)
red = (255, 0, 0)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
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

    screen.blit(image, (0, 0))
    x1 += x1_change
    y1 += y1_change

    # Check if snake hits the boundaries
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    pygame.draw.rect(screen, blue, [x1, y1, snake_block, snake_block])
    pygame.display.update()

    clock.tick(25)

if game_over:
    screen.blit(image, (0, 0))
    message("You lost", red)
    pygame.display.update()
    time.sleep(2)

pygame.quit()
quit()
