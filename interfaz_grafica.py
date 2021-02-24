import gamelib
import spades

ALTO_VENTANA, ANCHO_VENTANA = 480, 720

VERTICAL, HORIZONTAL = "v", "h"
RUTA_CARTA_DADA_VUELTA_HORIZONTAL = 
RUTA_CARTA_DADA_VUELTA_VERTICAL = 

ANCHO_CARTA = 103
ALTO_CARTA = 138

RUTA_PALO = {"D": "Diamond","C": "Hearts","P": "Spades","T": "Clubs"}

def dibujar_fondo():
    """
    Dibuja de fondo la imagen img/fondo.gif
    """
    gamelib.draw_image('img/fondo.png')

def mostrar_puntajes(juego):
    """
    Recibido un estado de juego, escribe los puntajes en la esquina superior izquierda.
    No devuelve nada
    """
    x, y = 10, 10
    for jugador in juego.jugadores:
        texto = f"{jugador}: {juego.jugadores[jugador].puntos}"
        draw_text(texto, x, y, size=12, **options)
        x += 10

def sel_img_carta(carta):
    """
    Recibe una carta y devuelve su imagen (la ubicacion en str).
    """
    numero = carta.mano
    palo = carta.palo
    return f"/img/{RUTA_PALO[palo]}_{numero}.gif"

def dibujar_carta(carta, x, y):
    """
    Recibida una Carta y coordenadas en pixeles, dibuja la carta en dicha posicion, no devuelve nada.
    """
    ruta_imagen = sel_img_carta(carta)
    gamelib.draw_image(f"{ruta_imagen}", x, y)

def dibujar_carta_tapada(x, y, orientacion):
    """
    Recibida una posicion en coordenadas en pixeles, dibuja una carta tapada en dicha posicion, no devuelve nada.
    El tercer elemento es si la carta esta en posicion VERTICAL u HORIZONTAL, si no corresponde a estas variables globales lanza una excepcion.
    """
    if orientacion != VERTICAL or orientacion != HORIZONTAL:
        raise FileNotFoundError

    gamelib.draw_image(f"/img/carta_dada_vuelta_{orientacion}", x, y)

def dibujar_cartas_tapadas(juego):
    """
    Recibido un estado de juego, dibuja las cartas tapadas de los jugadores de los cuales no es el turno actual.
    """
    for jugador in juego.jugadores:
        if not is turno de jugador:
            for _ in range(cantidad de cartas)
                dibujar_carta_tapada(posicion, )

def dibujar_cartas_turno(juego):
    """
    Recibido un estado de juego, dibuja las cartas del jugador actual.
    """
    inicio_vertical = ALTO_VENTANA # - (largo_carta)
    inicio_horizontal = ANCHO_VENTANA // 2 # - (cantidad_cartas//2) * ancho_carta

    #Todo lo que veas incompleto y en pseudocodigo es porque me faltaria mejorar lo de los objetos
    for carta in mano de jugador turno:
        dibujar_carta(carta, inicio_vertical, inicio_horizontal)
        inicio_horizontal += #le sumamos el ancho de cada carta dividido dos (asi se verian las cartas medio apiladas)

def mostrar_cartas(juego):
    """ 
    Dibuja por pantalla las cartas.
    No devuelve nada
    """
    dibujar_cartas_turno(juego)
    dibujar_cartas_tapadas(juego)

def mostrar_ganador():
    """
    Dibuja el ganador de la ronda.
    """
    pass

def mostrar_puntajes(juego):
    """
    Muestra los puntajes de cada jugador en pantalla ()
    """
    pass

def posicion_valida(x, y, juego):
    """
    Recibidas coordenadas en pixeles y un estado de juego, devuelve True si la posicion clickeada se encuentra entre las cartas de la mano, tambien verifica si la carta puede ser tirada o no.
    """
    turno = juego.turno_actual
    cartas = juego.jugadores[turno].

def carta_seleccionada(x, y):
    """
    Recibidas coordenadas en pixeles ()
    """
