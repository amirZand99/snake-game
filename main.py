import pygame

pygame.init()
screen = pygame.display.set_mode((800, 900))
image = pygame.image.load('/home/amir/Downloads/_400b86d6-92a7-40f4-b294-470887be9914.jpeg')
screen.blit(image, (0, 0))
pygame.display.update()
pygame.display.set_caption('Snake game by amir')
game_over=False

blue=(0,0,255)

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:  # Check if the user clicked the close button
            game_over = True  # Exit the game loop

    pygame.draw.rect(screen, blue, [300, 200, 20, 20])
    pygame.display.update()

pygame.quit()
quit()