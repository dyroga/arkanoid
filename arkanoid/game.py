import pygame


ANCHO_PANTALLA = 500
ALTO_PANTALLA = 600

class Arkanoid:

    def __init__(self):
        
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

    def jugar(self):

        salir = False

        while not salir:

            for evento in pygame.event.get():
                if pygame.QUIT == evento.type:
                    salir = True


            self.pantalla.fill((99, 0, 0))
            pygame.display.flip





        pygame.quit()

if __name__ == '__main__':
    print('arrancamos el juego desde arkanoid.py')
    juego = Arkanoid()
    juego.jugar()