import sys
import pygame
from rocket import Rocket

def move_rocket():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Rocket Moves")
	
	rocket = Rocket(screen)
	moving_right = False
	moving_left = False
	moving_up = False
	moving_down = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
				   moving_right = True
				   moving_left = False
				   moving_up = False
				   moving_down = False
				elif event.key == pygame.K_LEFT:
				   moving_right = False
				   moving_left = True   
				   moving_down = False
				   moving_up = False
				elif event.key == pygame.K_UP:
				   moving_right = False
				   moving_left = False   
				   moving_up = True
				   moving_down = False
				elif event.key == pygame.K_DOWN:
				   moving_right = False
				   moving_left = False   
				   moving_up = False
				   moving_down = True
			elif event.type == pygame.KEYUP:
				moving_right = False
				moving_left = False
				moving_up = False
				moving_down = False
		if moving_right and rocket.rect.right < rocket.screen_rect.right:
			rocket.rect.centerx = rocket.rect.centerx + 1
		elif moving_left and rocket.rect.left > 0:
			rocket.rect.centerx = rocket.rect.centerx - 1
		elif moving_up and rocket.rect.top > 0 :
			print(rocket.rect.top)
			rocket.rect.bottom = rocket.rect.bottom - 1
		elif moving_down and rocket.rect.bottom < rocket.screen_rect.bottom:
			rocket.rect.bottom = rocket.rect.bottom + 1
		#print("Rocket top - "+str(rocket.rect.bottom)+" screen top - "+str(rocket.screen_rect.bottom))
		screen.fill((255,255,255))
		rocket.blitme()
		pygame.display.flip()
move_rocket()				
				
		
		
		