# STANDAR
import os

# LIBRERIAR DE TERCEROS
import pygame as pg


# DEPENDENCIAS PROPIAS
from . import ALTO_PANTALLA, ANCHO_PANTALLA, FPS, VIDAS
from .entidades import ContadorVidas, Ladrillo, Pelota, Raqueta
from arkanoid.record import Records

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
        finalizar = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    finalizar = True
                    salir = True 
                elif evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        salir = True
                    elif evento.key == pg.K_ESCAPE:
                        salir = True
                        finalizar = True



            self.pantalla.fill((99, 0, 0))

            
            self.pintar_logo()
            self.pintar_mensaje()

            pg.display.flip()
        return finalizar

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
        self.reloj = pg.time.Clock()
        
        ruta = os.path.join('resources', 'images', 'background.jpg')
        self.fondo = pg.image.load(ruta)
        
        self.jugador = Raqueta()
        self.muro = pg.sprite.Group()
        self.pelota = Pelota(self.jugador)
        self.contador_de_vidas = ContadorVidas(VIDAS)

    
    def bucle_principal(self):
        super().bucle_principal()
        print('escena partida')

        finalizar = False
        salir = False
        estoy_jugando = False
        self.crear_muro()
       
        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True 
                elif evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        salir = True
                        finalizar = True
                    elif evento.key == pg.K_SPACE:
                        estoy_jugando = True
    
                        

            self.pintar_fondo()
            self.muro.draw(self.pantalla)
            
            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
        
            self.pelota.update(estoy_jugando)
            self.pantalla.blit(self.pelota.image, self.pelota.rect)

            if self.pelota.seguir:
                estoy_jugando = False
                salir = self.contador_de_vidas.perder_Vida()
                self.pelota.seguir = False




            golpeados = pg.sprite.spritecollide(self.pelota, self.muro, False)
            if len(golpeados) > 0:
                self.pelota.vel_y = -self.pelota.vel_y
                for ladrillo in golpeados:
                    ladrillo.update()

            pg.display.flip()
        return finalizar

    def pintar_fondo(self):
        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.fondo, (0, 800))
        self.pantalla.blit(self.fondo, (600, 0))
        self.pantalla.blit(self.fondo, (600, 800))

    def crear_muro(self):

        filas = 4
        columnas = 5
        margen_izquierdo = 10

        color = Ladrillo.ROJO
        for fila in range(filas):
            for columna in range(columnas):
                if color == Ladrillo.ROJO:
                    color = Ladrillo.VERDE
                else:
                    color = Ladrillo.ROJO
                ladrillo = Ladrillo(color)
                ancho_muro = ladrillo.rect.width * columnas
                margen_izquierdo = (ANCHO_PANTALLA - ancho_muro) // 2
                # izquierdo = (ANCHO_PANTALLA - (ladrillo.rect.width * columnas)) //2
                ladrillo.rect.x =  margen_izquierdo + columna  * (ladrillo.rect.width + 1)
                ladrillo.rect.y = (ladrillo.rect.height * 2) + fila * (ladrillo.rect.height + 1)
                self.muro.add(ladrillo)


    

class Puntuaciones(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta_letras = os.path.join('resources', 'fonts', 'CabinSketch-Bold.ttf')
        self.color_letra = 240, 220, 60
        self.alto_linea = 60
        self.letras =pg.font.Font(ruta_letras, self.alto_linea//3*2)
        self.margen_superior = ALTO_PANTALLA // 4
        self.margen = ANCHO_PANTALLA // 6


    def bucle_principal(self):
        super().bucle_principal()
        print('escena records')

        records = Records()
        records.cargar()
        print(records.game_records)

        linea = 0
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True 
            self.pantalla.fill((0, 99, 0))

            img_titulo = self.letras.render('RECORDS', True, self.color_letra)
            x = (ANCHO_PANTALLA - img_titulo.get_width())//2
            y = self.margen_superior // 2
            self.pantalla.blit(img_titulo, (x, y))

            linea = 0
            for record in records.game_records:
                nombre = record[0]
                puntos = str(record[1])

                img_nombre = self.letras.render(nombre, True, self.color_letra)
                x = self.margen
                y = self.margen_superior + self.alto_linea * linea
                self.pantalla.blit(img_nombre, (x, y))

                img_puntos = self.letras.render(puntos, True, self.color_letra)
                x = ANCHO_PANTALLA - self.margen - img_puntos.get_width()
                self.pantalla.blit(img_puntos, (x,y))

                linea += 1

            pg.display.flip()
