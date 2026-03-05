import math
import random
import pygame

# ======================
# CONSTANTS
# ======================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

PLAYER_SIZE = 64
ENEMY_SIZE = 70
BULLET_WIDTH = 20
BULLET_HEIGHT = 40

PLAYER_START_X = 370
PLAYER_START_Y = 380

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150

ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40

BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 30

# ======================
# INITIALIZE
# ======================
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")

icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# ======================
# BACKGROUND
# ======================
background = pygame.image.load('bg.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# ======================
# PLAYER
# ======================
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (PLAYER_SIZE, PLAYER_SIZE))

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# ======================
# ENEMY
# ======================
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _ in range(num_of_enemies):
    img = pygame.image.load('enemy.png')
    img = pygame.transform.scale(img, (ENEMY_SIZE, ENEMY_SIZE))
    enemyImg.append(img)

    enemyX.append(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# ======================
# BULLET
# ======================
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (BULLET_WIDTH, BULLET_HEIGHT))

bulletX = 0
bulletY = PLAYER_START_Y
bullet_state = "ready"

# ======================
# SCORE
# ======================
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

# ======================
# FUNCTIONS
# ======================
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # Center bullet on player
    screen.blit(bulletImg, (x + PLAYER_SIZE//2 - BULLET_WIDTH//2, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# ======================
# GAME LOOP
# ======================
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                bulletY = playerY
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - PLAYER_SIZE))

    # Enemy movement
    for i in range(num_of_enemies):

        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - ENEMY_SIZE:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Collision
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= BULLET_SPEED_Y

    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()