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
    velocidad = 10

    def __init__(self):
        super().__init__()

        self.imagenes = []
        for i in range(3):
            ruta_imagen = os.path.join('resources', 'images', f'electric0{i}.png')
            img = pg.image.load(ruta_imagen)
            self.imagenes.append(img)
        self.contador = 0

        self.image = self.imagenes[self.contador] 
        self.rect = self.image.get_rect()
        #self.rect.bottom = ALTO_PANTALLA - 25
        #self.rect.centerx = ANCHO_PANTALLA / 2
        self.rect.midbottom = (ANCHO_PANTALLA // 2, ALTO_PANTALLA - 25)


    def update(self):

        self.contador += 1
        if self.contador >= len(self.imagenes):
            self.contador = 0 
        self.image = self.imagenes[self.contador]

        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.x < 0:
                self.rect.x = 0
        if teclas[pg.K_RIGHT]:
            self.rect.x += self.velocidad
            if self.rect.right > (ANCHO_PANTALLA - 1):
                self.rect.right = (ANCHO_PANTALLA - 1)