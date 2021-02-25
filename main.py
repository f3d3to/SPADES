import interfaz_grafica
import spades
import gamelib

def juego_mostrar(juego):
    """
    Recibido un estado de juego lo muestra por pantalla
    """
    interfaz_grafica.dibujar_fondo()
    interfaz_grafica.mostrar_cartas(juego)
    interfaz_grafica.mostrar_puntajes(juego)
    interfaz_grafica.mostrar_turnos(juego)
    interfaz_grafica.mostrar_bazas(juego)
    interfaz_grafica.mostrar_apuestas(juego)

def apuesta_valida(juego, numero):
    """
    Verifica que un numero sea una apuesta valida. Siendo el numero necesario un numero entre 0 y numero_ronda
    """
    if numero == None or numero == "":
        return False
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for c in numero:
        if c not in numeros:
            return False
    n_ronda = juego.ronda.numero_ronda

    turno_actual = juego.turno_actual
    siguiente_turno = juego.siguiente_turno[turno_actual]
    primer_jugador = juego.primer_jugador

    if siguiente_turno == primer_jugador: #El turno actual es el ultimo jugador en tirar
        apuestas_totales = 1 #Empiezo en 1 porque el default del jugador sin apostar es -1
        for jugador in juego.jugadores:
            apuestas_totales += juego.jugadores[jugador].apuesta
        if int(numero) + apuestas_totales == juego.ronda.numero_ronda:
            print(f"EL NUMERO RONDA ES {juego.ronda.numero_ronda}, y las apuestas totales {apuestas_totales}")
            gamelib.say("Error, las apuestas totales no pueden coincidir con el numero de ronda.")
            return False

    return 0 <= int(numero) <= n_ronda

def pedir_apuestas(juego):
    """
    Recibido un estado de juego, le pide las apuestas a cada jugador y las guarda en dicho estado de juego.
    Devuelve un nuevo estado de juego
    """
    player = juego.turno_actual
    apuesta = gamelib.input(f"Ingrese su apuesta {player}")
    while not apuesta_valida(juego, apuesta):
        apuesta = gamelib.input(f"ERROR!\n{player}, ingrese una apuesta valida\nUn numero entre 0 y {juego.ronda.numero_ronda}")
    juego = spades.pedir_apuesta(juego, int(apuesta))
    return juego

def no_es_numero_correcto(numero):
    """
    Ingresado un numero, verifica si es un numero entre 2 y 4. Devuelve True en caso correcto, False en caso contrario.
    """
    return not numero in ["2", "3", "4"]

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
    for _ in range(int(numero_jugadores)):
        nombre = gamelib.input("INGRESE SU NOMBRE")
        while nombre == "" or nombre == None:
            gamelib.say("ERROR, DEBE INGRESAR UN NOMBRE")
            nombre = gamelib.input("INGRESE NUEVAMENTE SU NOMBRE")
        jugadores.append(nombre)

    return jugadores

def terminar_juego(juego):
    """
    Recibido un estado de juego, muestra por pantalla el ganador y muestra todas las puntuaciones
    """
    puntuaciones = ""
    for jugador in juego.jugadores:
        puntuaciones += f"{jugador}: {juego.jugadores[jugador].puntos}\n"
    ganador = spades.ganador(juego)
    gamelib.say(f"EL GANADOR ES {ganador}\n{puntuaciones}")

def main():
    gamelib.title("SPADES")
    juego = spades.crear_juego(juego_nuevo())
    gamelib.resize(interfaz_grafica.ANCHO_VENTANA, interfaz_grafica.
        ALTO_VENTANA)

    while gamelib.is_alive():

        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        if spades.juego_terminado(juego):
            terminar_juego(juego)
            juego = spades.crear_juego(juego_nuevo())

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
            
            if not juego.ronda.vuelta.numero_vuelta: #Si la vuelta es la 0
                juego = pedir_apuestas(juego)
                gamelib.say(f"Turno finalizado!\nPresionar OK para continuar")
                if spades.todos_apostaron(juego):
                    juego = spades.avanzar_vuelta(juego) #Se avanza a la vuelta 1 (primera)

            elif interfaz_grafica.posicion_valida(x, y, juego): #Se selecciono una carta valida
                carta = interfaz_grafica.carta_seleccionada(x, y, juego)
                juego = spades.tirar_carta(juego, carta)

            if len(juego.ronda.vuelta.cartas_puestas) == len(juego.jugadores): #Si todos jugaron sus cartas
                juego = spades.juego_actualizar(juego)

gamelib.init(main)