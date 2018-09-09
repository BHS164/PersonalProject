import pygame as pg
from Colours import *

# Initiate pygame
pg.init()
pg.mixer.init()

create a window
width = 1000
depth = 1000
screen = pg.display.set_mode((width, depth))
pg.display.set_caption('Entering Battle')

def fillScreen():
    
