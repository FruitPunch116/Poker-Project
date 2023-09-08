import pygame
import os
from os import listdir
from deck import deck
from player import player1
from player import dealer
from button import Button


class Hand():
    def __init__(self):
        deck.shuffle()
        deck.deal(player1)
        deck.deal(player1)
        deck.deal(dealer)
        deck.deal(dealer)
        self.stay = False
        self.hit = False
        self.over = False
        self.start = True
        start_amount = self.sumOfCards()
        print(self)
        print(f"Your total amount is {start_amount}. Do you want to hit or stay?")
    
    def __repr__(self):
        return f"{player1.name} has {player1.cards[0]} and {player1.cards[1]}"
    
    def sumOfCards(self):
        total_amount = 0
        
        for card in player1.cards:
        
            if card.value != 9 and card.value != 10 and card.value != 11 and card.value != 12:
                true_value = card.value
                true_value += 2
                
                total_amount+=true_value
            elif card.value == 12:
                if (total_amount + 11) > 21:
                    total_amount+=1
                elif (total_amount + 11) < 21:
                    total_amount+=11
            else:
                total_amount += 10
        
        return total_amount
    
    def action(self):
        print(self.hit_option())
        if self.sumOfCards() <= 21:
            print(f"Do you want to hit again or stay? Your new number is {self.sumOfCards()}")
        
        if self.sumOfCards() > 21:
                print(f"You total amount ({self.sumOfCards()}) is over 21, you lost")
    
    def hit_option(self):
        deck.deal(player1)        
        new_card = player1.cards[len(player1.cards) - 1]
    
        return f"{player1.name} selected hit and got {new_card}" 
        
hand = Hand()
# for card in player1.cards:
#     print(type(str(card)))

pygame.init()
pygame.display.set_caption("Blackjack")
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
main_menu_background = pygame.image.load("assets/blackjack_background.jpeg").convert_alpha()
screen_width, screen_height = pygame.display.get_surface().get_size()
background = pygame.transform.scale(main_menu_background, (screen_width, screen_height))
text_font = pygame.font.SysFont("Futura",60)
hit_image = None
stand_image = None

def draw_text(text, font, text_col, x, y):
    text = font.render(text, True, text_col)
    screen.blit(text, (x,y))
    
def display_first_hand(player):
    
    folder_dir = "/Users/larrytapia/Development/code/phase-3/Poker-Project/assets"
    
    player1_xCoordinate = 500
    player1_yCoordinate = 800
    
    dealer_xCoordinate = 1000
    dealer_yCoordinate = 300
    
    if player == dealer:
        for card in player.cards:
            
            if player.cards[0] == card:
                blind_card = pygame.image.load("assets/back_of_card.png").convert_alpha()
                blind_card = pygame.transform.scale(blind_card, (200,200))
                screen.blit(blind_card, (dealer_xCoordinate,dealer_yCoordinate))
                dealer_xCoordinate += 50
            else:
                for image in os.listdir(folder_dir):
                    if (image.startswith(str(card))):
                        card_image = pygame.image.load(f"assets/{image}").convert_alpha()
                        card_image = pygame.transform.scale(card_image, (200, 200))
                        screen.blit(card_image, (dealer_xCoordinate,dealer_yCoordinate))
                        dealer_xCoordinate += 50
    
    else:
        for card in player.cards:
            for image in os.listdir(folder_dir):
                if (image.startswith(str(card))):
                    card_image = pygame.image.load(f"assets/{image}").convert_alpha()
                    card_image = pygame.transform.scale(card_image, (200, 200))
                    screen.blit(card_image, (player1_xCoordinate,player1_yCoordinate))
                    player1_xCoordinate += 50
    

def blackjack_menu():
    
    while True:
        
        screen.blit(main_menu_background, (0,0))

        hit_image = pygame.image.load("assets/hand.png").convert_alpha()
        hit_image = Button(1250, 900, hit_image, 0.3)
        
        stand_image = pygame.image.load("assets/wave.png").convert_alpha()
        stand_image = Button(1500, 900, stand_image, 0.3)
        
        screen.blit(background, (0,0))
        hit_image.draw(screen)
        stand_image.draw(screen)
    
        for event in pygame.event.get():
            
            draw_text("HIT", text_font, (0,0,0), 1295, 1050)
            draw_text("STAND", text_font, (0,0,0), 1500, 1050)
            display_first_hand(player1)
            display_first_hand(dealer)

              
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if hit_image.clicked == True:
                hand.action()
                
            pygame.display.update()

blackjack_menu()

pygame.quit()