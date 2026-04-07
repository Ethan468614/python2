import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Set Window size (640, 480)
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 3. Set caption - My first game screen
pygame.display.set_caption("My first game screen")

# Define Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# 4. Display text setup
font = pygame.font.SysFont("Arial", 36)
text_surface = font.render("Hello Pygame!", True, BLACK)

# 5. Create a rectangle (positioned at the center)
# Rect format: [x, y, width, height]
rect_width, rect_height = 150, 100
rect_x = (screen_width // 2) - (rect_width // 2)
rect_y = (screen_height // 2) - (rect_height // 2)
my_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background - White
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, BLUE, my_rect)

    # Draw the text on the screen
    screen.blit(text_surface, (200, 50))

    # Update display
    pygame.display.flip()

pygame.quit()