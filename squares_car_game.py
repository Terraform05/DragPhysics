import pygame
from random import randint

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Car:
    def __init__(self, x, y):
        # Set the starting position of the car
        self.x = x
        self.y = y

    def update(self, keys):
        # Handle the key presses
        if keys[pygame.K_UP]:
            self.y -= 5
        if keys[pygame.K_DOWN]:
            self.y += 5
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5

    def draw(self, screen):
        # Draw the car
        pygame.draw.rect(screen, WHITE, [self.x, self.y, 20, 20])

class Game:
    def __init__(self):
        # Create a new car object
        self.car = Car(320, 240)

        # Create a list of objects
        self.objects = []
        for i in range(5):
            self.objects.append(pygame.Rect(randint(0, 640), randint(0, 480), 20, 20))

        # Initialize the game
        pygame.init()

        # Set the dimensions of the screen
        self.size = [640, 480]
        self.screen = pygame.display.set_mode(self.size)

        # Set the title of the window
        pygame.display.set_caption("Car game")

    def run(self):
        # Run the game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Get the current state of the keyboard
            keys = pygame.key.get_pressed()

            # Update the car
            self.car.update(keys)

            # Check if the car has collided with any of the objects
            for obj in self.objects:
                if self.car.x < obj.x + obj.width and self.car.x + 20 > obj.x:
                    if self.car.y < obj.y + obj.height and 20 + self.car.y > obj.y:
                        print("Game over!")
                        running = False

            # Fill the screen with black
            self.screen.fill(BLACK)

            # Draw the car
            self.car.draw(self.screen)

            # Draw the objects
            for obj in self.objects:
                pygame.draw.rect(self.screen, WHITE, obj)

            # Update the screen
            pygame.display.flip()

game = Game()
game.run()
