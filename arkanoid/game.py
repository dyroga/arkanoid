import pygame as pg

from . import ANCHO_PANTALLA, ALTO_PANTALLA
from .escenas import Partida, Portada, Puntuaciones

class Arkanoid:

    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

        portada = Portada(self.pantalla)
        partida = Partida(self.pantalla)
        puntuaciones = Puntuaciones(self.pantalla)

        self.escenas = [portada, partida, puntuaciones]

    def jugar(self):

        for escena in self.escenas:
            fin = escena.bucle_principal()
            if fin == True:
                break
       

        pg.quit()

if __name__ == '__main__':
    print('arrancamos el juego desde arkanoid.py')
    juego = Arkanoid()
    juego.jugar()