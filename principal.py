  #! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS1 import *
from extras import *
#!/usr/bin/env python




#Funcion principal

def main():


        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #tiempo total del juego
        gameClock = pygame.time.Clock()

        #inicializa el menu
        llamaMenu = menu()

        if llamaMenu == 3:
            pygame.quit()
            sys.exit()

        if llamaMenu == 1:
            pygame.init()
            archivo= open("lemario.txt","r",encoding='utf8')

        if llamaMenu == 2:

            pygame.init()
            archivo= open("lemario2.txt","r",encoding='utf8')
            pygame.init()


        tiempoMenu = pygame.time.get_ticks()/1000

        #Preparar la ventana
        pygame.display.set_caption("Armar palabras...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        totaltime = 0
        segundos = TIEMPO_MAX

        fps = FPS_inicial

        puntos = 0
        candidata = ""
        listaIzq = []
        listaMedio = []
        listaDer = []
        posicionesIzq = []
        posicionesMedio = []
        posicionesDer = []
        lista = []
        palabrasEncontradas=[]



        #archivo= open("lemario.txt","r")
        for linea in archivo.readlines():


            lista.append(linea[0:-1])


        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq ,
        posicionesMedio, posicionesDer)

        if llamaMenu == 1:
            dibujarAdultos (screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
            posicionesMedio, posicionesDer, puntos,segundos)
        else:
            dibujarNenes(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
            posicionesMedio, posicionesDer, puntos,segundos)

        sonido_fondo = pygame.mixer.Sound("fondo.wav")
        pygame.mixer.Sound.play(sonido_fondo)
        BACKGROUNDADULTOS= pygame.image.load("fondo1.png").convert()
        BACKGROUNDNENES= pygame.image.load("selva.jpg").convert()


        # TEMPORIZADOR
        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            if True:
                #aumenta la velocidad x fps a los 20y 40 seg
                print(totaltime, "totaltime")

                if segundos > 40:
                    fps = 2
                elif segundos > 20 and segundos < 40:
                    fps = 3
                elif segundos < 20:
                    fps = 4

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    candidata += letra
                    if e.key == K_BACKSPACE:
                        candidata = candidata[0:len(candidata)-1]
                    if e.key == K_RETURN:
                        puntos += procesar(lista, candidata, listaIzq, listaMedio, listaDer)
                        candidata = ""


            segundos = TIEMPO_MAX  + tiempoMenu - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior cambia fondos segun nivel
            if llamaMenu==1:

                 #cambia fondos segun nivel

                screen.blit(BACKGROUNDADULTOS, [0,0])

                #cambia fuentes segun nivel
                dibujarAdultos(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)

                pygame.display.flip()
            #maneja la distancia entre palabra y palabra
                actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq,
                    posicionesMedio, posicionesDer)
            else:
                #Limpiar pantalla  cambia fondos segun nivel
                screen.blit(BACKGROUNDNENES, [0,0])

                #Dibujar de nuevo todo cambia fuentes segun nivel
                dibujarNenes(screen, candidata, listaIzq, listaMedio, listaDer, posicionesIzq ,
                posicionesMedio, posicionesDer, puntos,segundos)
                pygame.display.flip()

                #maneja la distancia entre palabra y palabra
                actualizarnenes(lista, listaIzq, listaMedio, listaDer, posicionesIzq,
                posicionesMedio, posicionesDer)

        pygame.mixer.stop()
        sonido_final = pygame.mixer.Sound("final.wav")
        pygame.mixer.Sound.play(sonido_final)
        puntuacion(puntos)
        record(puntos,llamaMenu)

        muestraRecord(llamaMenu)

        # Cierra el archivo
        archivo.close()

##        while 1:
##            #Esperar el QUIT del usuario
##            for e in pygame.event.get():
##                if e.type == QUIT:
##                    pygame.quit()
##                    return
##Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

