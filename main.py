import pygame 
import sys 

pygame.init()
clock = pygame.time.Clock()


# setting up the main window 
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update window
    pygame.display.flip()
    clock.tick(60) # frames
