'''
Created on Nov 19, 2018

@author: venkat
'''
import sys
import pygame

def check_keydown_events(event,ship):
        #watch for keyboard and mouse events
                if event.key == pygame.K_RIGHT:
                    #Move the ship to right.
                    ship.moving_right = True    
                elif event.key == pygame.K_LEFT:
                    #Move the ship to right.
                    ship.moving_left = True    

def check_keyup_events(event,ship):
        #watch for keyboard and mouse events
                if event.key == pygame.K_RIGHT:
                    #Move the ship to right.
                    ship.moving_right = False    
                elif event.key == pygame.K_LEFT:
                    #Move the ship to right.
                    ship.moving_left = False    

def check_events(ship):
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ship)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)
                
def update_screen(ai_settings,screen,ship):
        # Redraw the screen during each pass through the loop.
        #screen.fill(ai_settings.bg_color)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
    