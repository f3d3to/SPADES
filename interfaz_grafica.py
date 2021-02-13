import gamelib

ANCHO = 100
LARGO = 700


def mostrar_estado_juego():
    """
    Recibe un estado de juego y
    """
    pass

def mostrar_ganador():
    pass

### MOSTRAR ESTADO DE JUEGO.
def p():
    """
    Dibuja el estdao
    """
    gamelib.resize(ANCHO, LARGO)
    while gamelib.loop():
        gamelib.draw_begin()
        gamelib.draw_end()
        for event in gamelib.get_events():
            if not event:
              break
            if event.type == gamelib.EventType.KeyPress:
              tecla = event.key
    gamelib.init(main)

p()