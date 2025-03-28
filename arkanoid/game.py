import pygame as pg

from . import ANCHO_PANTALLA, ALTO_PANTALLA


class Arkanoid:

    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

    def jugar(self):

        salir = False

        while not salir:

            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True


            self.pantalla.fill((99, 0, 0))
            pg.display.flip





        pg.quit()

if __name__ == '__main__':
    print('arrancamos el juego desde arkanoid.py')
    juego = Arkanoid()
    juego.jugar()