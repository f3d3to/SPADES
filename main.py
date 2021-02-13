## imports
import interfaz_grafica
import spades


def main():
    juego = inicializar_juego()
    while not juego.terminado():
        mostrar_estado_juego(juego)
        juego.mezclar_mazo()
        juego.repartir_cartas()
        juego.pedir_apuestas()
        while not juego.ronda_terminada():
            mostrar_estado_juego(juego)
            for jugador un juego.jugadores():
                jugador.pedir_jugada()
            juego.determinar_ganador_mano()
        juego.contabilizar_puntos_ronda()
    mostrar_ganador(juego)



## CLASES
"""
MAZO --> ¿? REPARTIDO|
CARTAS
CARTA_PRINCIPAL
TURNOS
JUGADOR
PUNTAJE
"""
## ESTADO DE JUEGO

## INTERFAZ GRAFICA --> IMAGENES ¿ROTADAS?