# TESTING PROCESS TO GET THE WINDOWS SIZE

import pygame
from classes.button import Button

pygame.init()
pygame.display.set_caption("Poker")
screen = pygame.display.set_mode((1750,900))
main_menu_background = pygame.image.load("assets/main_menu_background.jpeg").convert_alpha()
SCREEN_WIDHT, SCREEN_HEIGHT = pygame.display.get_surface().get_size()


background = pygame.transform.scale(main_menu_background, (SCREEN_WIDHT, SCREEN_HEIGHT))
text_font = pygame.font.SysFont("Baskerville",200)
start_button = None

def draw_text(text, font, text_col, x, y):
    text = font.render(text, True, text_col)
    screen.blit(text, (x,y))
    

def main_menu():
    pygame.display.set_caption("Poker Main Menu")
    
    while True:
        
        screen.blit(main_menu_background, (0,0))
        menu_mouse_position = pygame.mouse.get_pos()

        start_img = pygame.image.load("assets/start-button.png").convert_alpha()
        start_button = Button(725, 500, start_img, 0.5)
    
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
    
            screen.blit(background, (0,0))
            start_button.draw(screen)
            draw_text("FREE POKER", text_font, (255,255,255), 250, 150)
            pygame.display.update()

main_menu()

pygame.quit()