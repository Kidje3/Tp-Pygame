import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == 59:
        return("ñ")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, color)
    screen.blit(ren, posicion)

def dibujarAdultos (screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,posicionesMedio, posicionesDer, puntos,segundos):


    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)

    #Linea del piso
    pygame.draw.line(screen, (SPECIAL_BLUE), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #linea vertical
    pygame.draw.line(screen, (SPECIAL_BLUE), (2*ANCHO//3, ALTO-70) , (2*ANCHO//3, 0), 5)
    #linea vertical

    pygame.draw.line(screen, (SPECIAL_BLUE), (ANCHO//3, ALTO-70) , (ANCHO//3, 0), 5)

    ren1 = galaxy_font1.render(candidata, 1,YELLOW ) #LETRA ESCRIBE CANDIDATA
    ren2 = robotus_font.render("PunTos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos<15):
        ren3 = robotus_font.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = robotus_font.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

    for i in range(len(listaIzq)):
        screen.blit(galaxy_font.render(listaIzq[i], 1, COLOR_LETRAS), posicionesIzq[i])
    for i in range(len(listaMedio)):
        screen.blit(galaxy_font.render(listaMedio[i], 1, COLOR_LETRAS), posicionesMedio[i])
    for i in range(len(listaDer)):
        screen.blit(galaxy_font.render(listaDer[i], 1, COLOR_LETRAS), posicionesDer[i])

    screen.blit(ren1, (270, 550))
    screen.blit(ren2, (630, 10))
    screen.blit(ren3, (10, 10))


def dibujarNenes(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,posicionesMedio, posicionesDer, puntos,segundos):


    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)

    #Linea del piso
    pygame.draw.line(screen, (BROWN), (0, ALTO-48) , (ANCHO, ALTO-48), 5)

    #linea vertical
    pygame.draw.line(screen, (BROWN), (2*ANCHO//3, ALTO-48) , (2*ANCHO//3, 0), 5)
    #linea vertical

    pygame.draw.line(screen, (BROWN), (ANCHO//3, ALTO-48) , (ANCHO//3, 0), 5)


    ren1 = kids_font.render(candidata, 1, RED) #LETRA ESCRIBE CANDIDATA
    ren2 = wood_font.render("PunTos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos<15):
        ren3 = wood_font.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = wood_font.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

    for i in range(len(listaIzq)):
        screen.blit(titans_font.render(listaIzq[i], 1, COLOR_LETRASNENES), posicionesIzq[i])
    for i in range(len(listaMedio)):
        screen.blit(titans_font.render(listaMedio[i], 1, COLOR_LETRASNENES), posicionesMedio[i])
    for i in range(len(listaDer)):
        screen.blit(titans_font.render(listaDer[i], 1, COLOR_LETRASNENES), posicionesDer[i])

    screen.blit(ren1, (340, 550))
    screen.blit(ren2, (630, 10))
    screen.blit(ren3, (10, 10))