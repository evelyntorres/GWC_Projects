"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)



pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
pos = ()
#x_coor = random.randint(10, 30)
#y_coor = random.randint(10, 30)
colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]
Ball_color = BLACK
Ball_size = 30
x_speed = random.randint(-10, 10)
y_speed = random.randint(-10, 10)

x_location = random.randint(10, 30)
y_location = random.randint(10, 30)
ball_size = random.randint(10,30)

# WRITE YOUR CODE HERE








# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print("Here!")
		
			pos = pygame.mouse.get_pos() #returns (x, y)
			x_location, y_location = pos
			Ball_color = random.choice(colors)
			Ball_size = random.randint(20, 40)

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
	screen.fill(GREEN)

    # If you want a background image, replace this clear with blit'ing the
    # background image.
	
	# --- Drawing code should go here
	#pygame.draw.circle(screen, BLUE, [350, 250], 30,2 )

	#loop that adds/subtracts number from x,y
	#if pos:
	pygame.draw.circle(screen, Ball_color, [x_location, y_location], Ball_size) 
	if x_location >= screen_width - ball_size or x_location < ball_size:
		x_speed = x_speed * -1

	if y_location >= screen_height - ball_size or y_location < ball_size:
		y_speed = y_speed * -1

	x_location += x_speed 
	y_location += y_speed

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
