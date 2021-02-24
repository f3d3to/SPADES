# SPADES
Create for educational proposities. F.I.U.B.A.

## Comienzo de Juego

El juego de bazas puede jugarse de 2 a 4 jugadores, con naipes franceses, y consta de 13 rondas. En cada ronda, se le reparte a cada jugador una cantidad de cartas igual al número de ronda que se está jugando. En las rondas 1 a 12, luego de repartir las cartas, de develará la primer carta remanente del mazo y el palo de la misma será el palo del triunfo. En la ronda 13, el palo del triunfo es siempre Corazones.

## Apuesta

Al comienzo de cada ronda, y luego de ver sus cartas, cada jugador dirá cuántas "bazas" o manos va a ganar esa ronda. La única condición es que luego de que los 4 jugadores digan cuantas "bazas" va a ganar cada uno (pudiendo decir entre 0 y la cantidad de cartas que tenga en mano) la suma entre todos los jugadores debe ser distinta al número de ronda actual. Por lo tanto, el último jugador de la ronda está limitado en la cantidad de "bazas" que dice que puede ganar. Por ejemplo: habiendo 3 jugadores en la ronda 5, si el primer jugador dice que va a ganar 1 ronda, el segundo 3, el tercero, no puede decir 1 (porque sumaría 5). Debe decir cualquier otro número entre 0 y 5.

El primer jugador de la primer ronda es elegido al azar. A partir de la segunda ronda, el primer jugador es siempre el jugador que se encontraba a la izquierda del primero en la ronda anterior (es decir, el segundo).
Jugar las Cartas

En cada mano, después de que todos los jugadores hayan anunciado su apuesta, el que juegue primero jugará una de sus cartas (la que él quiera) y los demás deberán jugar una más en el mismo orden en que anunciaron su apuesta (de izquierda a derecha), y respetando las reglas siguientes:

* Si el jugador al que le toca jugar una carta tuviera una del palo con que el jugador mano (el primero en jugar) inició la baza, deberá jugarla superando el valor de las que ya se hubieran jugado, de las de ese palo.

* Si el jugador siguiente, no tuviera una carta del mismo palo con mayor valor, pero sí una de menor valor, debe jugar esa.

* Si no tuviera ninguna carta del palo de inicio, deberá jugar un triunfo si este fuera de valor superior al de otro triunfo que hubiera echado un adversario. Si no tuviera un triunfo para superar el ya existente, pero sí tuviera de valor inferior deberá jugarlo igualmente.

* Si no tuviera un triunfo entonces podrá jugar la carta que quisiera.

El orden de las cartas va dado según su numeración, salvo por el 1. De manera que el 2 es el que menos vale, luego el 3, etc. hasta el 10, luego la J, la Q, la K, y luego la carta de mayor valor es el 1. De manera que:
(2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < J < Q < K < 1).

## Puntaje

Al finalizar la ronda, se deben contabilizar los puntos ganados por cada jugador. Cada jugador ganará 10 puntos si adivinó el número exacto de bazas que se iba a llevar. Además, los jugadores que hubieran acertado en su previsión se llevarán 5 puntos por cada baza ganada en esa mano. Si un jugador apuestas que va a ganar 0 bazas, el mismo se llevará (además de los 10 puntos ya mencionados) 5 puntos multiplicado por el número de ronda que se haya jugado.
Ganar el Juego

Al finalizar la 12va ronda, el jugador con mayor puntaje, gana.
Requerimientos del TP

* El juego de Bazas debe poder ser jugado desde una computadora a través de una interfaz gráfica utilizando Gamelib.

* En el turno de cada jugador, se mostrarán únicamente las cartas del jugador actual (mostrando la parte de atrás de las de los demás jugadores que no les corresponda jugar).

La única diferencia con el juego real, es que al elegir las cartas para jugar cada mano, se irá de un jugador por vez en vez de todos al mismo tiempo (debido a limitaciones de mostrar todo en la misma pantalla).

## Notas

Notar que en esta implementación existe una clase Juego que tiene la mayoría del comportamiento. Queda a decisión del implementador decidir si utilizar esta u otras clases o no (recomendamos que usen al menos alguna clase porque les va a facilitar mantener el estado del juego).
