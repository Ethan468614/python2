import pygame
import random

pygame.init()

sprite_colur_change = pygame.USEREVENT + 1
background_colur_change = pygame.USEREVENT + 2


BLUE = pygame.Color('blue')
light_blue = pygame.Color('lightblue')
dark_blue = pygame.Color('darkblue')


YELLOW = pygame.Color('yellow')
MEGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):


    def __init__(self, colour,height,width):

        super().__init__()

        self.image = pygame.Surface([height,width])
        self.image.fill(colour)

        self.rect = self.image.get_rect()

        self.velocity = [random.randint(-1,1),random.randint(-1,1)]


    def update(self):

        self.rect.move_ip(self.velocity)

        boundary_hit = False  

        if self.rect.left < 0 or self.rect.right > 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if self.rect.top < 0 or self.rect.bottom > 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_colur_change))
            pygame.event.post(pygame.event.Event(background_colur_change))

    def change_colour(self):
        self.image.fill(random.choice([YELLOW, MEGENTA, ORANGE, WHITE]))


    def change_background_colour():
        global bg_clour

        bg_clour = random.choice([light_blue, dark_blue])


all_sprites_list = pygame.sprite.Group()                            
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)

all_sprites_list.add(sp1)

screen = pygame.display.set_mode([500,400])

pygame.display.set_caption('Boundary Sprite')

bg_clour = BLUE

screen.fill(bg_clour)

exit = False

clock = pygame.time.Clock()

while not exit:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == sprite_colur_change:
            sp1.change_colour()

        elif event.type == background_colur_change:
            background_colur_change()

all_sprites_list.update()

screen.fill(bg_clour)

all_sprites_list.draw(screen)

pygame.display.flip()

clock.tick(240)


pygame.quit()
               