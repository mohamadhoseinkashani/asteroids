from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from constants import PLAYER_RADIUS
import pygame
import sys
from shaping import CircleShape
from logger import log_state
from logger import log_event
import player
import asteroid
import asteroidsfield



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids,updatable,drawable)
    asteroidsfields = pygame.sprite.Group()
    asteroidsfield.AsteroidField.containers = (updatable, )

    player_character = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    

    asteroidsfield_object = asteroidsfield.AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
                        
        screen.fill("black")
        player_character.draw(screen)
        

        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
            if item.collides_with(player_character):
                if item == player_character:
                    continue
                log_event("player_hit")
                print("Game Over")
                sys.exit()

       
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        




if __name__ == "__main__":
    main()
