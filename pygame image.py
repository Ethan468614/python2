import pygame

pygame.init()

screenWidth, screenHeight = 500, 500

display_surface = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption('Adding background image')

background = pygame.transform.scale(
    pygame.image.load('background.jpg').convert(), (screenWidth, screenHeight))

cake = pygame.transform.scale(pygame.image.load('My chocolate cream cake.jpg').convert_alpha(), (200, 200))
cake_rect = cake.get_rect(center = (screenWidth//2, screenHeight//2 - 30))

def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        display_surface.blit(background, (0, 0))    
        display_surface.blit(cake, cake_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()            
        
