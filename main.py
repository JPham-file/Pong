import pygame 
import sys 

pygame.init()
clock = pygame.time.Clock()


# setting up the main window 
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update window
    pygame.display.flip()
    clock.tick(60)