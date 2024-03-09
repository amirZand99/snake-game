import pygame

pygame.init()
screen = pygame.display.set_mode((800, 900))
image = pygame.image.load('/home/amir/Downloads/_400b86d6-92a7-40f4-b294-470887be9914.jpeg')
screen.blit(image, (0, 0))
pygame.display.update()
pygame.display.set_caption('Snake game by amir')

game_over=False
paused = False

x1 = 400
y1 = 450

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

blue=(0, 0, 255)
white = (255, 255, 255)

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True
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
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT and not paused:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP and not paused:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN and not paused:
                y1_change = 10
                x1_change = 0

    screen.blit(image, (0, 0))

    x1 += x1_change
    y1 += y1_change
    # screen.fill(white)
    pygame.draw.rect(screen, blue, [x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(25)

pygame.quit()
quit()