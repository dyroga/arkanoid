import pygame as pg

from arkanoid.entidades import Pelota, Raqueta

pg.init()
pantalla = pg.display.set_mode((500,300))
reloj = pg.time.Clock()
raqueta = Raqueta()
pelota = Pelota(raqueta)

raqueta.rect.left = 70
raqueta.rect.y = 70

pelota.rect.left = 0
pelota.rect.y = 50

salir = False
cantidad = 0

while not salir:
    reloj.tick(8)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            salir = True

    pantalla.fill((50, 50, 50))

    pulsadas = pg.key.get_pressed()
    if pulsadas[pg.K_ESCAPE]:
        salir = True
    
    if pulsadas[pg.K_LEFT]:
        raqueta.rect.x -= 1
    if pulsadas[pg.K_RIGHT]:
        raqueta.rect.x += 1
    

    pantalla.blit(raqueta.image, raqueta.rect)
    pantalla.blit(pelota.image, pelota.rect)

    if pg.sprite.collide_rect(raqueta, pelota):
        print("colicion de rectangulos", cantidad)
        cantidad += 1

    if pg.sprite.collide_mask(raqueta, pelota):
        print("colicion de mascara", salir)

    pg.display.flip()
    



pg.quit()