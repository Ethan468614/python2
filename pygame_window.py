import pygame

# Initialize Pygame
pygame.init()

# 1. Window size (500, 500)
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# 2. Set caption
pygame.display.set_caption("My first game screen")

# 4. Background colour - Grey (58, 58, 58)
grey_color = (58, 58, 58)

# 3. Load and scale the image to (300, 300)
# Note: Replace 'your_image.png' with the actual path to your image file
try:
    original_image = pygame.image.load('image.png')
    image = pygame.transform.scale(original_image, (300, 300))
    
    # Calculate centre position
    # Position = (Screen_Width/2 - Image_Width/2, Screen_Height/2 - Image_Height/2)
    image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))
except:
    print("Please provide a valid image file path.")
    image = None

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(grey_color)

    # Draw the image at the calculated centre position
    if image:
        screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
