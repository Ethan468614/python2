import pygame
import random

# Initialize Pygame
pygame.init()

# 1. Set up the screen
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Add Custom Event")

# Define initial colors
WHITE = (255, 255, 255)

# 2. Create a Custom Event
# pygame.USEREVENT is the starting ID for custom events
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Set a timer to trigger the custom event every 2 seconds (2000 milliseconds)
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

# 3. Define the Sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Method to change color randomly
    def change_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(self.color)

# 4. Create two sprites
sprite1 = MySprite((255, 0, 0), 60, 60, 150, 150) # Starts Red
sprite2 = MySprite((0, 0, 255), 60, 60, 350, 150) # Starts Blue

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 5. Check if our Custom Event was triggered
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Background and Drawing
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    pygame.display.flip()

pygame.quit()