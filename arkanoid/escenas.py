# STANDAR
import os

# LIBRERIAR DE TERCEROS
import pygame as pg

# DEPENDENCIAS PROPIAS
from . import ALTO_PANTALLA, ANCHO_PANTALLA

class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        print('metodo vacio BUCLE_PRINCIPAL de escena ')

class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join('resources', 'images', 'arkanoid_name.png')
        self.logo = pg.image.load(ruta)

        ruta_letra = os.path.join('resources', 'fonts', 'CabinSketch-Bold.ttf')
        self.letra = pg.font.Font(ruta_letra, 25)

    def bucle_principal(self):
        super().bucle_principal()
        print('escena portada')

        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True 
            self.pantalla.fill((99, 0, 0))

            
            self.pintar_logo()
            self.pintar_mensaje()

            pg.display.flip()

    def pintar_mensaje(self):
        mensaje = "Pulsa SPACE para iniciar"
        img = self.letra.render(mensaje, True, (255, 255, 255))
        x = (ANCHO_PANTALLA - img.get_width()) // 2
        y = (ALTO_PANTALLA * 5) / 6
        self.pantalla.blit(img, (x, y))

    def pintar_logo(self):
        ancho, alto  = self.logo.get_size()
        x = (ANCHO_PANTALLA - ancho) // 2
        y = (ALTO_PANTALLA - alto) // 3
        self.pantalla.blit(self.logo, (x, y))

class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
    
    def bucle_principal(self):
        super().bucle_principal()
        print('escena partida')

        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True 
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()

class Puntuaciones(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        print('escena records')

        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True 
            self.pantalla.fill((0, 99, 0))
            pg.display.flip()
