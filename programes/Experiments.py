import pygame
import sys
# play area  get the screen
pygame.init() # instalizing the pygame

win = pygame.display.set_mode((400,400))

# backgroun img
backgroun_image = pygame.image.load("img.jpg")

# caption and Icon of frame
pygame.display.set_caption("my first-pygame")
icon = pygame.image.load("img.jpg")
pygame.display.set_icon(icon)
x=50
y=50
width = 40
height =60
velocity =10


def Gameover(v):
	if v==0 or v==360 or v==340:
		print("Game Over")
		pygame.quit()
		sys.exit()

run = True
while run:
	pygame.time.delay(100) # time delay in meli sec 
	for event in pygame.event.get(): # entring the user
			if event.type == pygame.QUIT: # user was cut the screen
				run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		if x==0:
			Gameover(x)

		x-=velocity
	if keys[pygame.K_RIGHT]:
		if x==360:
			Gameover(x)
		x+=velocity
	if keys[pygame.K_UP]:
		if y==0:
			Gameover(y)
		y-=velocity
	if keys[pygame.K_DOWN]:
		if y==340:
			Gameover(y)
		y+=velocity

	win.fill((0,0,0))
	win.blit(backgroun_image,(0, 0))

	pygame.draw.rect(win,(0,0,255), (x, y, width, height))
	pygame.display.update()

pygame.quit()

