import gamelib
import spades

ALTO_VENTANA, ANCHO_VENTANA = 700, 1050

ORIENTACION = {1: "v", 2: "h", 3: "h"}

ANCHO_CARTA = 103
ALTO_CARTA = 138
INICIO_UBICACION_CARTAS = (ANCHO_VENTANA - 14 * (ANCHO_CARTA/2)) // 2 #14 y no 13, para que quede centrada ya que la ultima carta se ve completa
SEPARACION_TEXTOS = 20
COLOR_TEXTO = "cyan"

RUTA_PALO = {"D": "Diamond", "C": "Hearts", "P": "Spades", "T": "Clubs"}


def dibujar_fondo():
    """
    Dibuja de fondo la imagen img/fondo.gif
    """
    gamelib.draw_image("img/fondo.gif", 0, 0)

def mostrar_puntajes(juego):
    """
    Recibido un estado de juego, escribe los puntajes en la esquina superior izquierda.
    No devuelve nada
    """
    tamaño_letra = SEPARACION_TEXTOS // 3 * 2
    x = y = ALTO_CARTA + SEPARACION_TEXTOS
    gamelib.draw_text(f"PUNTAJES", x, y, size=(tamaño_letra + tamaño_letra//3), fill=COLOR_TEXTO, anchor="w")
    y += SEPARACION_TEXTOS

    for jugador in juego.jugadores:
        texto = f"{jugador}: {juego.jugadores[jugador].puntos}"
        gamelib.draw_text(texto, x, y, size=tamaño_letra, anchor="w", fill=COLOR_TEXTO)
        y += SEPARACION_TEXTOS

def mostrar_turnos(juego):
    """
    Recibido un estado de juego, muestra el turno actual y el siguiente en la esquina inferior izquierda
    """
    tamaño_letra = SEPARACION_TEXTOS
    turno_actual = juego.turno_actual
    turno_siguiente = juego.siguiente_turno[turno_actual]
    y_texto_actual = ALTO_VENTANA - ALTO_CARTA - SEPARACION_TEXTOS * 2 - tamaño_letra
    y_texto_siguiente = y_texto_actual + SEPARACION_TEXTOS
    x = ALTO_CARTA + SEPARACION_TEXTOS

    gamelib.draw_text(f"Turno actual: {turno_actual}", x, y_texto_actual, size=tamaño_letra, fill=COLOR_TEXTO, anchor="w")
    gamelib.draw_text(f"Turno siguiente: {turno_siguiente}", x, y_texto_siguiente, size=tamaño_letra, fill=COLOR_TEXTO, anchor="w")

def sel_img_carta(carta):
    """
    Recibe una carta y devuelve su imagen (la ubicacion en str).
    """
    numero = carta.numero
    palo = carta.palo
    return f"img/{RUTA_PALO[palo]}_{numero}.gif"

def dibujar_carta(carta, x, y):
    """
    Recibida una Carta y coordenadas en pixeles, dibuja la carta en dicha posicion, no devuelve nada.
    """
    ruta_imagen = sel_img_carta(carta)
    gamelib.draw_image(f"{ruta_imagen}", x, y)

def dibujar_mano_tapada(n_posicion, jugador, juego):
    """
    Recibida un n_posicion (1, 2, 3) un jugador, y un estado de juego, dibuja la mano tapad aen la posicion indicada
    Posicion 1: arriba, Posicion 2: derecha, Posicion 3: izquierda
    """
    n_cartas = len(juego.jugadores[jugador].mano)

    if n_posicion == 1:
        separacion = ANCHO_CARTA // 2
        x_inicial = (ANCHO_VENTANA - (n_cartas+1) * (ANCHO_CARTA/2)) // 2
        y_inicial = 0

        for _ in range(n_cartas):
            gamelib.draw_image(f"img/Back_Red_1_{ORIENTACION[n_posicion]}.gif", x_inicial, y_inicial)
            x_inicial += separacion

    else:
        separacion = ANCHO_CARTA // 3 * 2 #2/3 de separacion
        y_inicial = (ALTO_VENTANA - (n_cartas+1) * (ANCHO_CARTA/3) * 2) // 2

        if n_posicion == 2:
            x_inicial = ANCHO_VENTANA - ALTO_CARTA
        if n_posicion == 3:
            x_inicial = 0

        for _ in range(n_cartas):
            gamelib.draw_image(f"img/Back_Red_1_{ORIENTACION[n_posicion]}.gif", x_inicial, y_inicial)
            y_inicial += separacion

def dibujar_cartas_tapadas(juego):
    """
    Recibido un estado de juego, dibuja las cartas tapadas de los jugadores de los cuales no es el turno actual, utilizando la funcion dibujar_mano_tapada
    """
    turno = juego.turno_actual
    cantidad_jugadores = len(juego.jugadores)
    n_jugador = 0

    for jugador in juego.jugadores:
        if jugador != turno:
            n_jugador += 1
            dibujar_mano_tapada(n_jugador, jugador, juego)

def dibujar_cartas_turno(juego):
    """
    Recibido un estado de juego, dibuja las cartas del jugador actual.
    """
    inicio_vertical = ALTO_VENTANA - ALTO_CARTA
    inicio_horizontal = INICIO_UBICACION_CARTAS
    separacion = ANCHO_CARTA // 2
    
    turno = juego.turno_actual

    for carta in juego.jugadores[turno].mano:
        dibujar_carta(carta, inicio_horizontal, inicio_vertical)
        inicio_horizontal += separacion

def mostrar_cartas(juego):
    """ 
    Dibuja por pantalla las cartas.
    No devuelve nada
    """
    dibujar_cartas_turno(juego)
    dibujar_cartas_tapadas(juego)
    dibujar_cartas_mesa(juego)
    dibujar_carta_triunfo(juego)

def dibujar_carta_triunfo(juego):
    """
    Recibido un estado de juego, si hay una carta triunfo en mesa, la dibuja.
    """
    if juego.ronda.no_hay_carta_triunfo():
        return
    dibujar_carta(juego.ronda.carta_triunfo)

def dibujar_cartas_mesa(juego):
    """
    Recibe un estado de juego.
    Dibuja las cartas de la mesa, 
    """
    n_jugadores = len(juego.jugadores)
    separacion = 30
    ancho_total = n_jugadores * ANCHO_CARTA + (n_jugadores - 1) * separacion
    x_inicio = (ANCHO_VENTANA - ancho_total) // 2
    alto_total = ALTO_CARTA
    y_inicio = (ALTO_VENTANA - alto_total) // 2

    for jugador in juego.ronda.vuelta.cartas_puestas:
        carta = juego.ronda.vuelta.cartas_puestas[jugador]
        gamelib.draw_text(jugador, x_inicio, y_inicio - separacion)
        dibujar_carta(carta, x_inicio, y_inicio)
        x_inicio += ANCHO_CARTA + separacion

def posicion_valida(x, y, juego):
    """
    Recibidas coordenadas en pixeles y un estado de juego, devuelve True si la posicion clickeada se encuentra entre las cartas de la mano, tambien verifica si la carta puede ser tirada o no.
    """
    turno = juego.turno_actual
    n_cartas = len(juego.jugadores[turno].mano)
    print("tengo cartas", n_cartas)
    y_inicial = ALTO_VENTANA - ALTO_CARTA
    y_final = ALTO_VENTANA
    x_inicial = INICIO_UBICACION_CARTAS
    x_final = x_inicial + (n_cartas + 1) * (ANCHO_CARTA / 2) #Nuevamente +1 porque la ultima carta se ve completa

    turno = juego.turno_actual

    if x_inicial < x < x_final and y_inicial < y < y_final:
        carta = carta_seleccionada(x, y, juego)
        if spades.carta_valida(juego, carta):
            return True

    return False

def i_carta_seleccionada(x, juego):
    """
    Recibidas coordenadas x en pixeles devuelve la posicion de carta que fue seleccionada (numero entero del indice de la mano)
    Pre: la posicion seleccionada esta dentro del espacio de cartas.
    """
    x_inicial = INICIO_UBICACION_CARTAS
    x -= x_inicial
    return x // (ANCHO_CARTA//2) - 1

def carta_seleccionada(x, y, juego):
    """
    Recibidas coordeanadas x y en pixeles y un estado de juego devuelve la carta seleccionada
    """
    turno = juego.turno_actual
    i = i_carta_seleccionada(x, juego)
    return juego.jugadores[turno].mano[int(i)]