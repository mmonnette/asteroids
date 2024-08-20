import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        #check for window closure
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #draw current game state on screen    
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

        #limit framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()