from arkanoid import ANCHO_PANTALLA, ALTO_PANTALLA
from arkanoid.game import Arkanoid

if __name__ == "__main__":
    print("arrancamos el juego arkanoid desde main.py")
    print(f'la pantalla tienne un ancho {ANCHO_PANTALLA} x {ALTO_PANTALLA}')
    juego = Arkanoid()
    juego.jugar()
