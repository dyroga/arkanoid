import os
from random import randint

import pygame as pg

from . import ALTO_PANTALLA, ANCHO_PANTALLA, VEL_MIN_Y, VEL_LIM_X, VEL_LIM_Y

class Raqueta (pg.sprite.Sprite):

    """
    1. es un sprite, usar herencia
    2. se puede mover
    3. se puede pintar en pantalla
    4. situarlo en la posicion inicial

    """
    velocidad = 15

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



IMAGENES = [
    pg.image.load(os.path.join('resources', 'images','greenTile.png')),
    pg.image.load(os.path.join('resources', 'images','redTile.png')),
    pg.image.load(os.path.join('resources', 'images','redTileBreak.png')),
]
class Ladrillo (pg.sprite.Sprite):

    VERDE = 0
    ROJO = 1
    ROJO_ROTO = 2

    def __init__(self, color=VERDE):
        super().__init__()
        self.tipo = color
        
        self.image = IMAGENES[color]
        self.rect = self.image.get_rect()

    def update(self):
        if self.tipo == Ladrillo.ROJO:
            self.tipo = Ladrillo.ROJO_ROTO
        else:
            self.kill()
        self.image = IMAGENES[self.tipo]


class Pelota(pg.sprite.Sprite):

    
    def __init__(self, raqueta):
        super().__init__()
        self.jugador = raqueta
        ruta = os.path.join('resources', 'images', 'ball1.png')
        self.image = pg.image.load(ruta)
        self.rect = self.image.get_rect()
        self.init_velocidades()
        self.seguir = False

        
    def update(self, estoy_jugando):
        if estoy_jugando == False:
            self.rect.midbottom = self.jugador.rect.midtop
        else:
            self.rect.x += self.vel_X
            self.rect.y += self.vel_y

            #rebota izquierda y derecha de la pantalla
            if self.rect.left <= 0 or self.rect.right >= ANCHO_PANTALLA:
                self.vel_X = -self.vel_X
            #rebota en la parte superior
            if self.rect.top <= 0 :
                self.vel_y = -self.vel_y
            
            #rebota en la raqueta
            if pg.sprite.collide_mask(self, self.jugador):
                self.init_velocidades()

            self.seguir = self.rect.top > ALTO_PANTALLA
          
    def init_velocidades(self):
        self.vel_X = randint(-VEL_LIM_X, +VEL_LIM_X)
        self.vel_y = randint(-VEL_LIM_Y, -VEL_MIN_Y)
        
    def pierdes (self):
        print('pierdes una vida')


class ContadorVidas :
    def __init__(self, vidas_iniciales):
        self.vidas = vidas_iniciales

    def perder_Vida(self):
        self.vidas -= 1
        print('has perdido una vida: te quedan ', self.vidas)
        return self.vidas == 0
    
    def pintar(self):
        pass