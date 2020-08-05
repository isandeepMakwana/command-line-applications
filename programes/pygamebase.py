import pygame

# play area  get the screen
pygame.init() # instalizing the pygame

win = pygame.display.set_mode((400,400))
pygame.display.set_caption("my first-pygame")




run = True
while run:
	for event in pygame.event.get(): # entring the user
			if event.type == pygame.QUIT: # user was cut the screen
				run = False

