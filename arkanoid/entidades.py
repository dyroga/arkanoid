import os

import pygame as pg

from . import ALTO_PANTALLA, ANCHO_PANTALLA

class Raqueta (pg.sprite.Sprite):
    """
    1. es un sprite, usar herencia
    2. se puede mover
    3. se puede pintar en pantalla
    4. situarlo en la posicion inicial

    """


    def __init__(self):
        super().__init__()

        self.image = []
        for i in range(2):
            ruta_imagen = os.path.join('resources', 'images', f'electric0{i}.png')

        ruta_imagen = os.path.join('resources', 'images', 'electric00.png')
        self.image = pg.image.load(ruta_imagen) 
        self.rect = self.image.get_rect()
        #self.rect.bottom = ALTO_PANTALLA - 25
        #self.rect.centerx = ANCHO_PANTALLA / 2
        self.rect.midbottom = (ANCHO_PANTALLA // 2, ALTO_PANTALLA - 25)


    def update(self): 
        pass