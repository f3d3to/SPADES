import gamelib
import spades


ANCHO = 100
LARGO = 700

def mostrar_ganador():
    pass


def sel_img_carta(carta):
    """
    Recibe una carta y devuelve su imagen.
    """
    pass

def mostrar_cartas():
    """ 
    Dibuja por pantalla las cartas.
    """
    
    gamelib.draw_image(f"/img/{sel_img_carta(carta)}.gif", x, y)

    #for cartas in Mano:

def mostrar_puntajes():
    pass

def mostrar_juego():
    pass

### MOSTRAR ESTADO DE JUEGO.
def mostrar_estado_juego(juego)():
    """
    Dibuja el estado de juego.
    """
    gamelib.resize(ANCHO, LARGO)
    while gamelib.loop():
        gamelib.draw_begin()
        mostrar_cartas()
        gamelib.draw_end()
        for event in gamelib.get_events():
            if not event:
              break
            if event.type == gamelib.EventType.KeyPress:
              tecla = event.key
    gamelib.init(main)