import pygame
from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():
    #initialize game and console a screen object
    print("Game starting")
    pygame.init()
    print("Pygame Initiated")
    ai_settings = Settings()
    print("Width - "+str(ai_settings.screen_width)+" Height - "+str(ai_settings.screen_height))
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship
    ship = Ship(ai_settings,screen)
    
    
    #start the main loop of the game
    while True:
        gf.check_events(ship)
        ship.update()        
        gf.update_screen(ai_settings, screen, ship)        
run_game()
    
