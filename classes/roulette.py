# import random

# class Roulette:

    # def __init__(self, number):
        # self.number = number

    # spin = random.randint(1,36)

    # if self.number % 2 == True:
        # odd
    # elif self.number % 2 == False:
        # even

    # print(spin)
    # def roulette_spin():
    #     money = 100

    #     while True:
    #         print(f"money left {money}")
    #         bet = int(input('How much do you wanna loose?'))
    #         print('')
    #         if bet > money:
    #             print('Go away you little bastard!')
    #             continue
    #         number = int(input("What's the number for your bet?"))
    #         if number < 0 or number > 36:
    #             print('No such a number allowed in the roulette.')
    #             continue
    #         money -= bet
    #         spin = random.randint(0,36)
    #         print('Congrats, now you have to pay taxes on your prize!')
    #         money += bet * 36
    #         else:
    #             print(f"{spin} House never loose budy, keep wwasting money!")
    #         if money <= 0:
    #             print('It seems to be like we made you go broke')
    #             break
    #         play_again = input('Do you still  want to make us more rich? (y/n)')
    #         if play_again.lower() == 'n':
    #             break
    #         # if play_again.lower() == 'y':
    #             # print
    # roulette_spin()

import pygame
import math
import random

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Roulette Wheel")

# Load roulette wheel image
wheel_image = pygame.image.load("../assets/Roulette.png").convert_alpha()

# Get the rect for the wheel image
wheel_rect = wheel_image.get_rect()
wheel_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Variables
angle = 0
spin_speed = 0
spinning = False

def spin_wheel():
    global angle, spin_speed, spinning
    angle = 9
    spin_speed = random.uniform(2, 5)  # Adjust the speed as needed
    spinning = True

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not spinning:
                spin_wheel()

    if spinning:
        angle += spin_speed
        if angle >= 360:
            angle = 0
            spinning = False

    screen.fill(WHITE)
    rotated_wheel = pygame.transform.rotate(wheel_image, angle)
    wheel_rect = rotated_wheel.get_rect(center=wheel_rect.center)
    screen.blit(rotated_wheel, wheel_rect.topleft)

    pygame.display.flip()

pygame.quit()
