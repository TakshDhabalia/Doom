import pygame as pg 
from settings import * 


class Object_renderer:
    def __init__ (self , game):
        self.game = game
        self .screen = game.screen
        self.wall_textures = self.load_wall_textures()

    @staticmethod
    def get_texture(path):
        res=(TEXTURE_SIZE, TEXTURE_SIZE)
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)
    def load_wall_textures(self):
        return {
            1: self.get_texture('D:\SEM_4\Python_mini_project/resources/textures/1.png'),
            2: self.get_texture('./resources/textures/2.png'),
            3: self.get_texture('./resources/textures/3.png'),
            4: self.get_texture('./resources/textures/4.png'),
            5: self.get_texture('./resources/textures/5.png'),
        }