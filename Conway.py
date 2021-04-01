import pygame
import time
import random
import numpy as np

#poorly done but i tried

gameover= False

height = 500
width = 500

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame!")
clock = pygame.time.Clock()


cellsCountWidth = 25
cellsCountHeight = 25
cellWidth = width / cellsCountWidth             # screen width divided by how many cells you wnat in the x axis
cellHeight = height / cellsCountHeight           # screen height divided by how many cells you want in the y axis

# 0,0
#
#
#
#          10,10...

def drawGrid(grid):
    x=y=0
    screen.fill(black)
    # only draws squares that is "alive"
    for line in range(cellsCountHeight-1):
        for cell in range(cellsCountWidth-1):
            color = white
            if grid[x][y] == 1:
                pygame.draw.rect(screen, color, (x*cellWidth, y*cellHeight, cellWidth, cellHeight))
            x+=1
        y+=1
        x=0



grid = [[random.randint(0, 1) for i in range(cellsCountWidth)] for i in range(cellsCountHeight)]
grid2 = [[0 for i in range(cellsCountWidth)] for i in range(cellsCountHeight)]

def updateCell():
    for y in range(1, cellsCountHeight-1):
        for x in range(1, cellsCountWidth-1):
            neightbours = (grid[x-1][y-1] + grid[x][y-1] + grid[x+1][y-1] +
                           grid[x-1][y] + grid[x+1][y] +
                           grid[x-1][y+1] + grid[x][y+1] + grid[x+1][y+1])
            # count how many neightbours is alive to determine the next generation
            if grid[x][y] == 1 and neightbours < 2 or neightbours > 3:
                grid2[x][y] = 0
            elif neightbours == 3:
                grid2[x][y] = 1
    # copy the new generation to the last grid
    # because the new generation cannot affect the ongoing change
    # so we need to have 2 grids so 1 doesnt affect the other
    for i in range(cellsCountHeight):
        for j in range(cellsCountWidth):
            grid[j][i] = grid2[j][i]
    drawGrid(grid)


tick = 0

while not gameover:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True


    updateCell()

    pygame.display.update()
    clock.tick_busy_loop(30)

pygame.quit()
