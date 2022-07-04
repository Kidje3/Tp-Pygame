from principal import *
from configuracion import *
from extras import *
import random
import math

palabrasEncontradas=[]
palabrasMostradas = []
# -*- coding: utf-8 -*-

def cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):

    z= random.randint(0,len(lista)-1)
    palabra_elegida= lista [z]

    # Bucle para no mostrar palabras repetidas

    while palabra_elegida in palabrasMostradas:
        z= random.randint(0,len(lista)-1)
        palabra_elegida= lista [z]

    # Si no está repetida la graba en la lista para comparar futuras palabras

    palabrasMostradas.append(lista[z])

    cont=0
    print(palabra_elegida)
    borde= len(palabra_elegida)//3
    y=35

    #listas aux almacenan SOLO las posiciones de la palabra elegida y se vacian al terminar

    auxIzq=[]
    auxDer=[]
    auxMedio=[]

    for letra in palabra_elegida:
        if cont < borde:
            listaIzq.append(letra)
            cont= cont +1
            x= random.randint(1,240)

            if len(posicionesIzq)==0: #si es la primer letra le asigna x directo
                auxIzq.append([x,y])   #tmb la guarda en aux para evaluar las siguientes
                posicionesIzq.append([x,y])
            else:  #va a evaluar la x de la letra con las x de las anteriores
                while estaCerca(x, auxIzq)==True:
                    #evalua si la x se repite en alguna de las posiciones guardadas en aux
                    x= random.randint(1,240)
                posicionesIzq.append([x,y]) #una vez q ya no se repite append en ambas
                auxIzq.append([x,y])

        elif cont >= borde and cont < (borde*2):
            listaMedio.append(letra)
            cont= cont + 1
            x= random.randint(270,510)

            if len(posicionesMedio)==0:
                auxMedio.append([x,y])
                posicionesMedio.append([x,y])
            else:
                while estaCerca(x, auxMedio)==True:
                    x= random.randint(270,510)
                posicionesMedio.append([x,y])
                auxMedio.append([x,y])

        else:

            listaDer.append(letra)
            cont=cont+1
            x= random.randint(550, 780)
            auxDer.append([x,y])

            if len (posicionesDer)==0:
                auxDer.append([x,y])
                posicionesDer.append([x,y])
            else:

                while estaCerca(x, auxDer)==True:
                        x= random.randint(550,780)
                posicionesDer.append([x,y])
                auxDer.append([x,y])
    print (auxDer, auxIzq ,auxMedio)
    auxDer=[]
    auxIzq=[]
    auxMedio=[]
    print (auxDer,"*", auxIzq ,"*",auxMedio)

def bajar(lista, posiciones):

    # hace bajar las letras y elimina las que tocan el piso
    i=0
    while i < (len (lista)):
        if (posiciones [i][1] < 501):
            posiciones [i][1]= posiciones[i][1]+15
            i=i+1
        else:
            lista.pop(i)
            posiciones.pop(i)


def actualizar(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    ## llama a otras funciones para bajar bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)
    bajar(listaIzq,posicionesIzq)
    bajar(listaMedio,posicionesMedio)
    bajar(listaDer,posicionesDer)


    if posicionesDer [-1][1]>90 : #si Y de la ultima letra de la palabra anterior ya bajo 70
                                    # vuelve a cargar con palabra nueva
        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)

def actualizarnenes(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer):
    ## llama a otras funciones para bajar bajar las letras, eliminar las que tocan el piso y
    ## cargar nuevas letras a la pantalla (esto puede no hacerse todo el tiempo para que no se llene de letras la pantalla)
    bajar(listaIzq,posicionesIzq)
    bajar(listaMedio,posicionesMedio)
    bajar(listaDer,posicionesDer)

    if posicionesDer [-1][1]>150 : #si Y de la ultima letra de la palabra anterior ya bajo 70
                                    # vuelve a cargar con palabra nueva
        cargarListas(lista, listaIzq, listaMedio, listaDer, posicionesIzq , posicionesMedio, posicionesDer)


def estaCerca(elem, lista):
    #es opcional, se usa para evitar solapamientos

    for i in range (0,len(lista)):
        dife= elem - lista[i][0]

        if abs(dife) <  TAMANNO_LETRA -5 : #evalua segun variable tamaño letra (extras) =20
            return True
    return False


def Puntos(candidata):
    suma=0
    vocales="aeiou"
    dificiles= "jkqwxyz"
    # realiza la suma para los puntajes acumulkando los valores de las letras

    for letra in candidata:
        if letra in vocales:
            suma = suma + 1
        else:
            if letra in dificiles:
                suma= suma +5
            else:
                suma= suma + 2
    return suma


def procesar(lista, candidata, listaIzq, listaMedio, listaDer):
    #chequea que candidata sea correcta en cuyo caso devuelve el puntaje y 0 si no es correcta

    if esValida(lista, candidata, listaIzq, listaMedio, listaDer)==True and candidata not in palabrasEncontradas:
        palabrasEncontradas.append(candidata)
        # Reproduce un sonido si es correcta
        sonido_correcta = pygame.mixer.Sound("correcta.wav")
        pygame.mixer.Sound.play(sonido_correcta)

        return Puntos(candidata)


    else:
        sonido_mal = pygame.mixer.Sound("mal.wav")
        pygame.mixer.Sound.play(sonido_mal)
        return 0


def esValida(lista, candidata, listaIzq, listaMedio, listaDer):
    cadena=""
    if candidata not in lista:
        return False
    else:
        palabrasEnPantalla=[listaIzq,listaMedio,listaDer]
        valida=True
        for letra in candidata:
            if letra in palabrasEnPantalla[0]:
                ()
            else:
                palabrasEnPantalla[0]=[]
                if letra in palabrasEnPantalla[1]:
                    ()
                else:
                    palabrasEnPantalla[1]=[]
                    if letra in palabrasEnPantalla[2]:
                        ()
                    else:
                        valida=False
        return (valida)

def menu():

    screen = pygame.display.set_mode((ANCHO, ALTO))
    width = screen.get_width()
    height = screen.get_height()

    imagen_boton_salir= pygame.transform.scale(pygame.image.load("salir.png"), (320, 120))
    imagen_boton_adultos = pygame.transform.scale(pygame.image.load("adultos.png"), (320, 120))
    imagen_boton_ninos = pygame.transform.scale(pygame.image.load("ninos.png"), (320, 120))

    mueve = 1

    while True :
        image=pygame.image.load("background.jpg").convert()
        screen.blit(image, (0, 0))
        screen.blit(imagen_boton_adultos ,(width/2-160,75))
        screen.blit(imagen_boton_ninos ,(width/2-160,250))
        screen.blit(imagen_boton_salir,(width/2-160,425))

        for e in pygame.event.get():

            #Ver si fue apretada alguna tecla

            if e.type == KEYDOWN:

                if e.key == K_DOWN:
                    if mueve < 3:
                        mueve = mueve + 1

                    else:
                        mueve = 1
                if e.key == K_UP:
                    if mueve > 1:
                        mueve = mueve -1
                    else:
                        mueve = 3

                if e.key == K_RETURN or e.key == K_SPACE:

                    return(mueve)
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

        if mueve == 1:
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(248, 78, 308, 108),1)
        if mueve == 2:
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(248, 252, 308, 108),1)
        if mueve == 3:
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(248, 430, 308, 108),1)
        pygame.display.update()

def puntuacion(puntos):
    puntaje = int(puntos)

    screen = pygame.display.set_mode((ANCHO, ALTO))
    smallfont = pygame.font.SysFont('Arial',35)
    color = (255,255,255)

    # ver esto

    width = screen.get_width()
    height = screen.get_height()
##    imagen_boton = pygame.transform.scale(pygame.image.load("boton.jpg"), (160, 60))

    text1 = smallfont.render('Juego Terminado' , True , color)
    text2 = smallfont.render('Su puntaje fue' , True , color)
    text3 = smallfont.render(str(puntaje) , True , color)
    text4 = smallfont.render("Presione una tecla para continuar" , True , color)

    while True :

        image=pygame.image.load("background.jpg").convert()

        screen.blit(image, (0, 0))

        screen.blit(text1 ,(290,height/3.8))
        screen.blit(text2 ,(300,height/2.7))
        screen.blit(text3 ,(width/2-10,height/1.95))
        screen.blit(text4 ,(180,height/1.5))

        pygame.display.update()
        for e in pygame.event.get():

            if e.type == KEYDOWN:
                pygame.quit()
                return()


def record(puntos, dificultad):

    listaRecord = []
    variable = ""
    contador = 0
    puntaje = int(puntos)

    # Abre el archivo en modo lectura

    if dificultad == 1:

        archivo = open("record.txt", "r")

    else:
        archivo = open("record-infantil.txt", "r")

        # Lee linea por linea y lo almacena en una lista. Usa strip para eliminar el salto

    for linea in archivo:
        listaRecord.append(linea.strip("\n"))

        # Cierra el archivo

    archivo.close()

    # Si el puntaje es el mayor lo almacena primero y desplaza al resto y mueve
    # el contador para que entre en los otros if y para marcar que modifico un valor

    if puntaje > int(listaRecord[1]):
        nombre = capturaNombre()
        listaRecord[4] = listaRecord[2]
        listaRecord[5] = listaRecord[3]
        listaRecord[2] = listaRecord[0]
        listaRecord[3] = listaRecord[1]
        listaRecord[0] = nombre
        listaRecord[1] = puntaje
        contador = 1

    # Si el puntaje es el segundo lo almacena y desplaza al siguiente y mueve
    # el contador para que entre en los otros if y para marcar que modifico un valor

    if puntaje > int(listaRecord[3]) and contador == 0:
        nombre = capturaNombre()
        listaRecord[4] = listaRecord[2]
        listaRecord[5] = listaRecord[3]
        listaRecord[2] = nombre
        listaRecord[3] = puntaje
        contador = 1

    # Si el puntaje es el tercero lo almacena y elimina el otro y mueve
    # el contador para que entre en los otros if y para marcar que modifico un valor

    if puntaje > int(listaRecord[5]) and contador == 0:
        nombre = capturaNombre()
        listaRecord[4] = nombre
        listaRecord[5] = puntaje
        contador = 1


    # Abre el archivo para escritura solo si el puntaje es mayor a alguno de los existentes
    # lo verifica con el contador

    if contador == 1 :
        if dificultad == 1:
            archivo = open("record.txt", "w")
        else:
            archivo = open("record-infantil.txt", "w")

        # Graba la lista en el archivo
        for i in range(len(listaRecord)):
            archivo.write(str(listaRecord[i]))
            archivo.write("\n")

        # Cierra el archivo
        archivo.close()
    return()

def muestraRecord(dificultad):
    pygame.font.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    smallfont = pygame.font.SysFont('Arial',35)
    color = (255,255,255)
    lista = []
    # ver esto

    width = screen.get_width()
    height = screen.get_height()

    if dificultad == 1:

        archivo = open("record.txt", "r")

    else:
        archivo = open("record-infantil.txt", "r")

        # Lee linea por linea y lo almacena en una lista. Usa strip para eliminar el salto

    for linea in archivo:
        lista.append(linea.strip("\n"))

        # Cierra el archivo

    archivo.close()

    text1 = smallfont.render(lista[0], True , color)
    text2 = smallfont.render(str(lista[1]), True , color)
    text3 = smallfont.render(lista[2], True , color)
    text4 = smallfont.render(str(lista[3]), True , color)
    text5 = smallfont.render(lista[4], True , color)
    text6 = smallfont.render(str(lista[5]), True , color)
    text7 = smallfont.render("Presione una tecla para continuar" , True , color)
    text8 = smallfont.render("Mejores Puntajes" , True , color)



    # muestra en pantalla los textos

    while True :
        image=pygame.image.load("background.jpg").convert()
        screen.blit(image, (0, 0))
        screen.blit(text1 ,(width/2-200,height/4))
        screen.blit(text2 ,(width/2+170,height/4))
        screen.blit(text3 ,(width/2-200,height/2.3))
        screen.blit(text4 ,(width/2+170,height/2.3))
        screen.blit(text5 ,(width/2-200,height/1.60))
        screen.blit(text6 ,(width/2+170,height/1.6))
        screen.blit(text7 ,(180,height/1.2))
        screen.blit(text8 ,(285,height/9))

        pygame.display.update()
        for e in pygame.event.get():

            if e.type == KEYDOWN:

                pygame.quit()
                return(True)

def capturaNombre():
    pygame.init()
    # prepara la pantalla

    screen = pygame.display.set_mode((ANCHO, ALTO))
    smallfont = pygame.font.SysFont('Arial',35)
    color = (255,255,255)
    nombreGanador = ""
    # ver esto
    width = screen.get_width()
    height = screen.get_height()
    text1 = smallfont.render("¡¡¡Felicitaciones!!!", True , color)
    text2 = smallfont.render("¡¡¡Lograste uno de los mejores puntajes!!!", True , color)
    text3 = smallfont.render("Ingresá tu nombre y presiona ENTER", True , color)

    while True :
        image=pygame.image.load("background.jpg").convert()
        screen.blit(image, (0, 0))

        # muestra en pantalla los textos
        screen.blit(text1 ,(width/2-110,height/8))
        screen.blit(text2 ,(width/2-265,height/3))
        screen.blit(text3 ,(width/2-240,height/1.8))

        pygame.display.update()

    #Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

        #Ver si fue apretada alguna tecla

            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                nombreGanador += letra
                if e.key == K_BACKSPACE:
                    tamanio = len(nombreGanador)
                    nombreGanador = nombreGanador[:tamanio-1]
        # Si apreto ENTER devuelve el nombre

                if e.key == K_RETURN:
                    return(nombreGanador)

        text4 = smallfont.render(nombreGanador, True , color)
        screen.blit(text4 ,(width/2-50,height/1.4))
        pygame.display.update()