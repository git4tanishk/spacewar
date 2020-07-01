import pygame
import sys
import os
import random

# intilize pygame
pygame.init()
resource_path="";

current_path = os.path.dirname(__file__) # your .py file is located
# print(current_path)
image_path_1 = os.path.join(current_path, 'spaceship.png') # the image folder path
print(current_path)

# creating screen 
screen = pygame.display.set_mode((800, 600))

# background image 
image_path_4 = os.path.join(current_path, '2352.jpg') # the image folder path
backgroundimg = pygame.image.load(image_path_4)
# backgroundimg = pygame.image.load(C:\\Users\\news4\\Desktop\\Tanishkk\\pygames\\game1\\2352.jpg)

pygame.display.set_caption("space fight ")
# icon = pygame.image.load("C:\\Users\\news4\\Desktop\\Tanishkk\\pygames\\game1\\spaceship.png")

# title and icon
icon = pygame.image.load(image_path_1)
pygame.display.set_icon(icon)

# player image
image_path_2 = os.path.join(current_path, 'space-invaders.png') # the image folder path
playerimg = pygame.image.load(image_path_2)
# playerimg = pygame.image.load(C:\\Users\\news4\\Desktop\\Tanishkk\\pygames\\game1\\space-invaders.png)

# monster image 
image_path_3 = os.path.join(current_path, 'monster.png') # the image folder path
monsterimg = pygame.image.load(image_path_3)
# playerimg = pygame.image.load(C:\\Users\\news4\\Desktop\\Tanishkk\\pygames\\game1\\space-invaders.png)

# player
player_x = 370
player_y = 480
player_x_change = 0.3

# monster
monster_x = random.randint(0, 800)
monster_y = random.randint(50, 150)
monster_x_change = 0.3 
monster_y_change = 40


def player(player_x, player_y):
    screen.blit(playerimg, (player_x, player_y))

def monster(monster_x, monster_y):
    screen.blit(monsterimg, (monster_x, monster_y))

Running = True

# game loop
while Running:

    # screen colour 
    screen.fill((0, 0, 0))

    # background image 
    screen.blit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Running = False
            sys.exit()
            break

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3 
            if event.key == pygame.K_RIGHT:
                player_x_change = +0.3 
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                player_x_change = 0 

    player_x += player_x_change
    
    monster_x += monster_x_change
    # player boundry
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736 :
        player_x = 736

    # monster movements 
    if monster_x <= 0:
        monster_x_change = 0.3
        monster_y += monster_y_change
    elif monster_x >= 736 :
        monster_x_change = -0.3
        monster_y += monster_y_change

    # images 
    player(player_x, player_y)
    monster(monster_x, monster_y)
    pygame.display.update()
    
