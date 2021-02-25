PALOS = "D", "C", "P", "T" 
CARTAS = 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", 1
RONDA_FINAL = 12

import gamelib
from random import randrange

class Jugador:
	def __init__(self, nombre):
		self.nombre = nombre
		self.mano = []
		self.puntos = 0
		self.apuesta = -1
		self.bazas = 0
		
	def sumar_bazas(self):
		"""
		Suma una baza
		"""
		self.bazas += 1
	
	def reiniciar_apuesta(self):
		"""
		Reinicia la puesta del jugador (-1)
		"""
		self.apuesta = -1

	def reiniciar_bazas(self):
		"""
		Reinicia las bazas a 0
		"""
		self.bazas = 0
		
	def asignar_apuesta(self, apuesta):
		"""
		Recibida una apuesta la asigna a self.apuesta
		"""
		self.apuesta = apuesta

	def limpiar_mano(self):
		"""
		Limpia la mano de cartas
		"""
		self.mano = []

	def agregar_carta(self, carta):
		"""
		Recibe una carta del tipo Carta y la agrega a su mano
		"""
		self.mano.append(carta)

	def sacar_carta(self, carta):
		"""
		Recibe una carta del tipo Carta y la quita de su mano, la devuelve.
		Condicion: la carta debe estar en la mano
		"""
		self.mano.remove(carta)
		return carta

	def sumar_puntos(self, puntos):
		"""
		Recibe puntos (int) y los suma
		"""
		self.puntos += puntos

class Juego:
	def __init__(self, jugadores):
		"""
		Recibe una lista jugadores, y le da los siguientes atributos:
		self.ronda del objeto tipo Ronda
		self.jugadores el cual es un diccionario con claves de nombre y valores un objeto del tipo Jugador()
		"""
		self.ronda = Ronda()
		self.jugadores = {}

		siguiente_turno = {}
		for i_jugador in range(len(jugadores)): #Creo un diccionario con los siguientes turnos de cada jugador
			if i_jugador == len(jugadores) - 1:
				siguiente_turno[jugadores[i_jugador]] = jugadores[0]
			else:
				siguiente_turno[jugadores[i_jugador]] = jugadores[i_jugador+1]

		self.siguiente_turno = siguiente_turno

		primer_jugador = jugadores[randrange(len(jugadores)-1)]

		self.turno_actual = self.primer_jugador = primer_jugador
		for jugador in jugadores:
			self.jugadores[jugador] = Jugador(jugador)

	def repartir(self, mazo):
		"""
		Reparte self.ronda cartas a cada jugador descontandolas del mazo(lista de Cartas) recibido.
		Devuelve el mazo restante
		"""
		for jugador in self.jugadores:
			for i in range(self.ronda.numero_ronda):
				i_carta_random = randrange(len(mazo)-1)
				carta_sacada = mazo.pop(i_carta_random)
				self.jugadores[jugador].agregar_carta(carta_sacada)
		return mazo

	def siguiente_ronda(self):
		"""
		Avanza a la siguiente ronda.
		"""
		self.primer_jugador = self.siguiente_turno[self.primer_jugador]
		self.turno_actual = self.primer_jugador
		self.ronda.avanzar()

class Carta:
	def __init__(self, numero=None, palo=None):
		"""
		Recibe numero entero y palo en formato str
		"""
		self.palo = palo
		self.numero = numero

	def es_mayor(self, otra):
		"""
		Recibida otra carta, devuelve True si self > otra y False si self < otra (hablando de los numeros ordenados segun la lista global CARTAS)
		"""
		i_self = 0
		i_otra = 0
		for i in range(len(CARTAS)):
			if self.numero == CARTAS[i]:
				i_self = i
			if otra.numero == CARTAS[i]:
				i_otra = i
		return i_self > i_otra

	def carta_nula(self):
		"""
		Verifica si una carta es nula, es decir si su palo y numero son None
		"""
		return self.palo == None and self.numero == None

	def __eq__(self, otra):
		"""
		Dos cartas son iguales si tienen el mismo palo y el mismo numero
		"""
		return self.palo == otra.palo and self.numero == otra.numero

	def mismo_palo(self, otra):
		"""
		Recibe otra carta del mismo tipo, devuelve True si son del mismo palo, False si son distinto.
		"""
		return self.palo == otra.palo
		
class Ronda:
	def __init__(self):
		self.numero_ronda = 1
		self.carta_triunfo = Carta()
		self.vuelta = Vuelta()

	def asignar_carta_triunfo(self, carta_triunfo):
		"""
		Recibe una carta y la asigna a la carta triunfo
		"""
		self.carta_triunfo = carta_triunfo

	def no_hay_carta_triunfo(self):
		"""
		Si self.carta_triunfo == -1, devuelve True, en caso contrario devuelve False
		"""
		return self.carta_triunfo.carta_nula()

	def avanzar(self):
		"""
		Avanza a la siguiente ronda
		"""
		self.carta_triunfo = Carta()
		self.numero_ronda += 1

class Vuelta:
	def __init__(self):
		self.carta_mesa = Carta()
		self.ganador_vuelta = None
		self.numero_vuelta = 0
		self.cartas_puestas = {}

	def agregar_carta_mesa(self, carta, jugador):
		"""
		Agrega una carta a la mesa, al diccionaro cartas_puestas, donde usa a la carta como clave y valor al jugador. Si el diccionario esta vacio (la carta tirada es la primera de la mesa) se agrega a self.carta_mesa
		No devuelve nada
		"""
		if self.carta_mesa.carta_nula():
			self.carta_mesa = carta
		self.cartas_puestas[jugador] = carta

	def avanzar(self):
		"""
		Avanza el numero de vuelta, reinicia todas las cartas_puestas en la mesa
		No devuelve nada
		"""
		self.numero_vuelta += 1
		self.cartas_puestas = {}
		self.carta_mesa = Carta()

	def mesa_vacia(self):
		"""
		Devuelve True si no hay cartas en la mesa, si hay cartas devuelve False
		"""
		return not len(self.cartas_puestas)

	def reiniciar_vueltas(self):
		"""
		Reinicia las vueltas a 0. (porque se cambio de ronda). Quita la carta mesa.
		"""
		self.numero_vuelta = 0
		self.carta_mesa = Carta()


def mazo_completo():
	"""
	No recibe nada, devuelve una lista de Cartas representando el mazo completo
	"""
	mazo = []

	for numero in CARTAS:
		for palo in PALOS:
			mazo.append(Carta(numero, palo))

	return mazo


def repartir_cartas(juego, mazo):
	"""
	Recibe un mazo y un estado de juego.
	Devuelve una tupla, (juego, mazo_sobrante)
	"""
	return juego, juego.repartir(mazo)

def crear_juego(jugadores):
	"""
	Recibe una lista con cada nombre de jugador y crea y devuelve un nuevo estado de juego del tipo Juego.
	"""
	juego = Juego(jugadores)
	juego, mazo_sobrante = repartir_cartas(juego, mazo_completo())
	juego = carta_triunfo(juego, mazo_sobrante)
	return juego

def juego_actualizar(juego):
	"""
	Recibe un estado de juego y lo actualiza avanzando una vuelta.
	Devuelve el nuevo estado de juego.
	Precondicion: el juego no debe estar terminado.
	"""
	juego = vuelta(juego)
	if juego.ronda.vuelta.numero_vuelta == juego.ronda.numero_ronda:
		return avanzar_ronda(juego)
	return avanzar_vuelta(juego)

def bazas_a_0(juego):
	"""
	Recibido un estado de juego, reinicia las bazas de todos los jugadores a 0
	"""
	for jugador in juego.jugadores:
		juego.jugadores[jugador].reiniciar_bazas()
	return juego

def avanzar_ronda(juego):
	#Aca hay que verificar las apuestas y sumar esos puntos y reiniciamos apuestas
	juego = verificar_puntuaciones(juego)
	juego = quitar_apuestas(juego)

	juego.ronda.vuelta.reiniciar_vueltas()
	
	juego = bazas_a_0(juego)

	juego.siguiente_ronda()

	juego, mazo_sobrante = repartir_cartas(juego, mazo_completo())

	if juego.ronda.numero_ronda == RONDA_FINAL:
		carta_corazones = Carta("A", "C")
		juego = carta_triunfo(juego, carta_corazones)
	else:
		juego = carta_triunfo(juego, mazo_sobrante)
	return juego

def avanzar_vuelta(juego):
	"""
	Avanza la vuelta, devuelve el nuevo estado de juego.
	Preconodicion, las vueltas no deben superar al numero de rondas
	"""
	juego.ronda.vuelta.avanzar()
	return juego

def vuelta(juego):
	"""
	Recibido un estado de juego, realiza la comprobacion final de la vuelta.
	Precondicion, todas las cartas de la "vuelta" deben estar sobre la mesa
	Aclaracion: No avanza la vuelta, eso lo hace la funcion avanzar_vuelta(juego)
	"""
	jugador_ganador = determinar_ganador_mano(juego)
	gamelib.say(f"EL GANADOR DE LA BAZA FUE\n{jugador_ganador}")
	juego.jugadores[jugador_ganador].sumar_bazas()
	juego.turno_actual = jugador_ganador
	return juego

def tirar_carta(juego, carta):
	"""
	Pone la carta en mesa del jugador, cambia turno y saca dicha carta de la mano del jugador.
	Si es el primer turno, la carta se agrega al atributo de la vuelta del juego carta_mesa
	Precondicion: la carta debe estar en la mano del jugador del turno actual. 
	"""
	turno_actual = juego.turno_actual
	juego.jugadores[turno_actual].mano.remove(carta)
	juego.ronda.vuelta.agregar_carta_mesa(carta, turno_actual)
	juego.turno_actual = juego.siguiente_turno[turno_actual]

	return juego

def carta_triunfo(juego, mazo):
	"""
	Recibido un estado de juego y un mazo sobrante (lista de Cartas), saca una al azar y actualiza la carta triunfo del estado de juego
	"""
	i_carta = randrange(len(mazo))
	carta = mazo[i_carta]
	juego.ronda.asignar_carta_triunfo(carta)
	return juego

def pedir_apuesta(juego, apuesta):
	"""
	Recibe una apuesta int, la asigna al jugador del turno actual del juego.
	Cambia a turno siguiente
	Devuelve un nuevo estado de juego
	"""
	turno = juego.turno_actual
	juego.jugadores[turno].apuesta = apuesta
	juego.turno_actual = juego.siguiente_turno[turno]
	
	return juego

def todos_apostaron(juego):
	"""
	Recibido un estado de juego verifica si todos apostaron, en caso positivo devuelve True, en caso contrario, devuelve False
	"""
	for jugador in juego.jugadores:
		if juego.jugadores[jugador].apuesta == -1:
			return False
	return True

def quitar_apuestas(juego):
	"""
	Recibido un estado de juego reinicia todas las apuestas de los jugadores.
	"""
	for jugador in juego.jugadores:
		juego.jugadores[jugador].apuesta = -1
	return juego

def verificar_puntuaciones(juego):
	"""
	Recibido un estado de juego verifica si algun jugador coincidio su numero de bazas. Verifica todas las puntuaciones
	Devuelve un nuevo estado de juego
	"""
	ronda = juego.ronda.numero_ronda
	for jugador in juego.jugadores:
		apuesta = juego.jugadores[jugador].apuesta
		bazas = juego.jugadores[jugador].bazas
		if apuesta == bazas:
			juego.jugadores[jugador].puntos += 10 + 5 * bazas
			if apuesta == 0:
				juego.jugadores[jugador].puntos += 5 * ronda
	return juego

def juego_terminado(juego):
	"""
	Recibido un estado de juego, devuelve True si el juego esta terminado, False si no.
	"""
	return juego.ronda.numero_ronda == RONDA_FINAL + 1

def ganador(juego):
	"""
	Recibido un estado de juego, devuelve el jugador ganador.
	"""
	jugador_ganador = juego.turno_actual #Empiezo con un turno ganado

	for jugador in juego.jugadores:
		if juego.jugadores[jugador].puntos > juego.jugadores[jugador_ganador].puntos:
			jugador_ganador = jugador
	return jugador

def tiene_carta_mesa(juego):
	"""
	Recibido un estado de juego, devuelve True si el jugador del turno actual tiene una carta del mismo palo que el palo de carta de apertura en su mano. False en caso contrario
	"""
	turno_actual = juego.turno_actual
	for carta in juego.jugadores[turno_actual].mano:
		if carta.mismo_palo(juego.ronda.vuelta.carta_mesa):
			return True
	return False

def tiene_carta_triunfo(juego):
	"""
	Recibido un estado de juego, devuelve True si el jugador del turno actual tiene una carta del palo triunfo, False en caso contrario.
	"""
	turno_actual = juego.turno_actual
	for carta in juego.jugadores[turno_actual].mano:
		if carta.mismo_palo(juego.ronda.carta_triunfo):
			return True
	return False

def carta_mayor_palo(juego, carta):
	"""
	Recibido un estado de juego, devuelve True si la carta elegida es la mayor del palo en la mano
	"""
	turno_actual = juego.turno_actual
	for c in juego.jugadores[turno_actual].mano:
		if carta.mismo_palo(c):
			if c.es_mayor(carta):
				return False
	return True

def carta_valida(juego, carta):
	"""
	Recibido un estado de juego y una carta, devuelve True si la carta es valida para tirar, False si no lo es.
	"""
	turno_actual = juego.turno_actual
	n_cartas_mano = len(juego.jugadores[turno_actual].mano)
	if juego.ronda.vuelta.mesa_vacia(): #Si es el primero en tirar
		return True

	carta_apertura = juego.ronda.vuelta.carta_mesa 
	carta_triunfo = juego.ronda.carta_triunfo

	if carta.mismo_palo(carta_apertura):
		if carta_mayor_palo(juego, carta):
			return True
		return False

	if not tiene_carta_mesa(juego):
		if carta.mismo_palo(carta_triunfo):
			if carta_mayor_palo(juego, carta):
				return True
			return False
		if not tiene_carta_triunfo(juego):
			return True

	return False

def le_gana(juego, carta1, carta2):
	"""
	Recibido un estado de juego y dos cartas las compara, si carta1 es mayor a carta2 devuelve True, sino devuelve False
	Aclaracion: existe la posibilidad que la carta sea la misma (ya que puede coincidir con el caso base en determinar_ganador_mano), en ese caso devuelve false.
	"""
	if carta1 == carta2:
		return False

	palo_triunfo = juego.ronda.carta_triunfo.palo
	palo_apertura = juego.ronda.vuelta.carta_mesa.palo

	if carta1.palo == palo_triunfo:
		if carta2.palo == palo_triunfo:
			return carta1.es_mayor(carta2)
		return True

	if carta1.palo == palo_apertura:
		if carta2.palo == palo_triunfo:
			return False
		if carta2.palo == palo_apertura:
			return carta1.es_mayor(carta2)

	#La carta1 es de uno de los otros dos palos
	if carta2.palo == palo_triunfo or carta2.palo == palo_apertura:
		return False

	#La carta2 tambien es uno de los otros dos palos
	return carta1.es_mayor(carta2)


def determinar_ganador_mano(juego):
	"""
	Recibido un estado de juego, determina quien fue el ganador de la mano.
	Devuelve el nombre del jugador.
	"""
	jugador_ganador = juego.turno_actual
	carta_ganadora = juego.ronda.vuelta.cartas_puestas[jugador_ganador]

	for jugador in juego.ronda.vuelta.cartas_puestas:
		carta = juego.ronda.vuelta.cartas_puestas[jugador]
		if le_gana(juego, carta, carta_ganadora):
			carta_ganadora = carta
			jugador_ganador = jugador

	return jugador_ganador