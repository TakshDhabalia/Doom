import pygame as pg 
import random 
import moderngl
import sys
from settings import *
from map import *

#my day one documentation is going to be so bad cause i just made a mesh rn 

#this class got all the main methods required for the game
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)#resolution from settings file
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)#to initialize the map and to put the basic vals in
    
    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):
        self.screen.fill('black')#bg fill
        self.map.draw()

    def check_events(self):#to add the main exit loop and its basically esc or ctrl+c
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:#while the game is running do this
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()

            
