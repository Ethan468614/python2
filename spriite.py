import pygame

# Initialize Pygame
pygame.init()

# 1. Set up the screen (640x480)
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Add Sprites Project")

# Define Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 2. Define the Sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

# 3. Create two rectangular sprites
sprite1 = MySprite(RED, 50, 50, 100, 100)  # The controllable sprite
sprite2 = MySprite(GREEN, 50, 50, 300, 200) # The stationary sprite

# Group the sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Main Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. Movement controls for sprite1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        sprite1.move(5, 0)
    if keys[pygame.K_UP]:
        sprite1.move(0, -5)
    if keys[pygame.K_DOWN]:
        sprite1.move(0, 5)

    # Drawing
    screen.fill(WHITE)
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60) # Limits to 60 frames per second

pygame.quit()