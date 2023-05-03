import pygame
from pygame.locals import *


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    """A class representing a car sprite"""

    def __init__(self):
        super().__init__()

        # Load the car image and make it smaller
        self.image = pygame.image.load("car.png")
        self.image = pygame.transform.smoothscale(self.image, (50, 25))

        # Flip the car horizontally
        self.image = pygame.transform.flip(self.image, False, True)

        # Set the initial position of the car
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        """Update the car's position based on the player's input"""

        # Check for events
        for event in pygame.event.get():
            # Quit the game if the player closes the window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Rotate the car when the player presses the arrow keys
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    self.rect.y -= 10
                elif event.key == K_DOWN:
                    self.rect.y += 10
                elif event.key == K_LEFT:
                    self.image = pygame.transform.rotate(self.image, -90)  # Rotate the car left
                elif event.key == K_RIGHT:
                    self.image = pygame.transform.rotate(self.image, 90)  # Rotate the car right


def main():
    # Initialize PyGame
    pygame.init()

    # Set the size of the game window
    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))

    # Create a car sprite
    car = Car()

    # Add the car sprite to the screen
    all_sprites = pygame.sprite.Group()
    all_sprites.add(car)

    # Game loop
    while True:
        # Update the car's position
        car.update()

        # Update the screen
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
