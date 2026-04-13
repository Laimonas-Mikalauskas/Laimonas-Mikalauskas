import pygame
import sys
import random

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Defense of Trappist 1D')
clock = pygame.time.Clock()

# Game variables
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50]
enemies = [[random.randint(0, SCREEN_WIDTH), 0] for _ in range(10)]
bullet_pos = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_pos.append(player_pos[0])  # Bullet fired from player position

    # Move the enemies
    for enemy in enemies:
        enemy[1] += 5  # Move enemy down
        if enemy[1] > SCREEN_HEIGHT:
            enemy[0] = random.randint(0, SCREEN_WIDTH)  # Respawn enemy
            enemy[1] = 0

    # Move the bullets
    for i in range(len(bullet_pos)):
        bullet_pos[i] -= 10  # Move bullet left

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (0, 255, 0), (player_pos[0], player_pos[1], 50, 50))

    # Draw the enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], 50, 50))

    # Draw the bullets
    for bullet in bullet_pos:
        pygame.draw.rect(screen, (255, 255, 0), (bullet, player_pos[1], 10, 5))

    pygame.display.flip()
    clock.tick(FPS)
