import interfaz_grafica
import spades

def juego_mostrar(juego):
    """
    Recibido un estado de juego lo muestra por pantalla
    """
    interfaz_grafica.dibujar_fondo()
    interfaz_grafica.mostrar_cartas(juego)
    interfaz_grafica.dibujar_avatars(juego)
    interfaz_grafica.mostrar_puntajes(juego)

def pedir_apuestas(juego):
    """
    Recibido un estado de juego, le pide las apuestas a cada jugador y las guarda en dicho estado de juego.
    """
    pass

def no_es_numero_correcto(numero):
    """
    Ingresado un numero, verifica si es un numero entre 2 y 4. Devuelve True en caso correcto, False en caso contrario.
    """
    return numero in ["2", "3", "4"]

def juego_nuevo():
    """
    Crea un nuevo estado de juego, y pregunta a usuario cuantos jugadores van a ser y pregunta sus respectivos nombres.
    Devuelve una lista con todos esos nombres
    """
    numero_jugadores = gamelib.input("INGRESE EL NUMERO DE JUGADORES")
    while no_es_numero_correcto(numero_jugadores):
        gamelib.say("ERROR, DEBE INGRESAR UN NUMERO ENTRE 2 Y 4")
        numero_jugadores = gamelib.input("INGRESE NUEVAMENTE EL NUMERO DE JUGADORES")

    jugadores = []
    for _ in rannge(int(numero_jugadores))
        nombre = gamelib.input("INGRESE SU NOMBRE")
        while nombre == "" or nombre == None:
            gamelib.say("ERROR, DEBE INGRESAR UN NOMBRE")
            nombre = gamelib.input("INGRESE NUEVAMENTE SU NOMBRE")
        jugadores.append(nombre)

    return jugadores

def main():
    juego = spades.crear_juego(juego_nuevo())

    gamelib.resize(interfaz_grafica.ANCHO_VENTANA, interfaz_grafica.
        ALTO_VENTANA)

    while gamelib.is_alive():

        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            #x, y = pixel_a_cartesiano(x, y)
            if posicion_valida(x, y): #Aca comprobaria si selecciono una carta el jugador actual, si selecciona una carta:
                juego = juego_actualizar(Carta)
            
