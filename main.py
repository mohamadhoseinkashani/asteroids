from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from constants import PLAYER_RADIUS
import pygame
from logger import log_state
import player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player_character = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
                        
        screen.fill("black")
        player_character.draw(screen)
        player_character.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        




if __name__ == "__main__":
    main()
