import sys
import pygame

def key_detect():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption('Keys Display')
	largeText = pygame.font.Font('freesansbold.ttf',115)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				text = chr(event.key)
				TextSurf = largeText.render(text,True,(0,0,0))
				TextRect = TextSurf.get_rect()
				TextRect.center = (600,400)
				screen.fill((230,230,230))
				screen.blit(TextSurf, TextRect)
				pygame.display.flip()
key_detect()	