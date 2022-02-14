import pygame
import random
import time

# driver code
pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# screen vars
w, h = 800, 800
n = 50
array = random.sample(range(100, 701), n)
com = 0
it = 0
sc = 0

# min width of block
x = w // n

print("starting visualizer ...")
time.sleep(1)

s = time.time()

for i in range(n):
	it += i
	for j in range(n-i-1):
		# core bubble sort logic
		if array[j] > array[j+1]:
			array[j+1], array[j] = array[j], array[j+1]
			com += 1

		# var updates
		e = time.time()

		f = e-s
		it += j
		sc += 1

		# clear canvas and re-draw data
		screen.fill((0, 0, 0))

		for k in range(n):
			pygame.draw.rect(screen, [255, 255, 255], [k*x, h-array[k], x, array[k]], 1)

		pygame.draw.rect(screen, [0, 255, 0], [j*x, 0, x, h])

		# check for exit events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		# update canvas
		pygame.display.update()

		# update info related to the algo and the program
		pygame.display.set_caption(f"TimeElapsed:{f:.2f}  Comparisons:{com}  Iterations:{it}  Canvas Refreshes:{sc}")

		# wait next refresh
		time.sleep(0.02)

# just for leaving the display open after visualization is over
while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()

	pygame.display.flip()
