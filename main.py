import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycating import *
from obj_renderer import *
from sprite_object import *
from object_handler import *
from wepon import *
from sound import *
from pathfinder import *
import asyncio

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.event.set_grab(True)#confining function
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        asyncio.run(self.setup())

    async def setup(self):
        await self.new_game()

    async def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)
        await asyncio.sleep(0)

    async def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        await asyncio.sleep(0)

    async def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        await asyncio.sleep(0)
        # self.map.draw()
        # self.player.draw()

    async def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)
            await asyncio.sleep(0)

    async def run(self):
        while True:
            await self.check_events()
            await self.update()
            await self.draw()
            await asyncio.sleep(0)

if __name__ == '__main__':
    game = Game()
    asyncio.run(game.run())
