PALOS = "D", "C", "P", "T" 
CARTAS = 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", 1
RONDA_FINAL = 13
CARTA_CORAZONES = Carta("A", "C")

from random import randrange

class Jugador:
	def __init__(self, nombre):
		self.nombre = nombre
		self.mano = []
		self.puntos = 0
		self.apuesta = 0
		self.bazas = 0
		self.carta_tirada = None
		
	def sumar_bazas(self):
		"""
		Suma una baza
		"""
		self.bazas += 1
	
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
		#hacer diccionario con siguiente turno
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
				jugador.mano.agregar_carta(carta_sacada)
		return mazo

	def siguiente_ronda(self):
		"""
		Avanza a la siguiente ronda, devuelve el estado de juego.
		"""
		primer_jugador = siguiente_turno[primer_jugador]
		self.ronda.avanzar()
		return juego

class Carta:
	def __init__(self, numero, palo):
		self.palo = palo
		self.numero = numero

	def comparar(self, carta_triunfo, lista_de_cartas):
		"""decide la ganadora"""
		
class Ronda:
	def __init__(self):
		self.numero_ronda = 0
		self.palo_triunfo = None
		self.vuelta = Vuelta()

	def carta_triunfo(self, carta_triunfo = None):
		"""
		Recibe una carta entre CORAZONES, DIAMANTE, PICA, TREVOL y lo asigna a la carta triunfo
		Si no recibe nada, se considera que el palo ganador es CORAZONES
		"""
		self.carta_triunfo = carta_triunfo

	def avanzar(self):
		"""
		Avanza a la siguiente ronda
		"""
		self.ronda += 1

class Vuelta:
	def __init__(self):
		self.carta_mesa = carta_mesa
		self.ganador_vuelta = None
		self.numero_vuelta = 0
		self.cartas_mesa = {}

	def agregar_carta_mesa(self, carta, jugador):

	def avanzar_vuelta(self):
		self.numero_vuelta += 1
		self.cartas_mesa = {}
		return juego

	def primer_carta(self, carta):
		self.carta_mesa = carta_mesa

	def reinicar_vueltas(self):
		self.numero_vuelta = 0

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
	juego, mazo_sobrante = repartir_cartas(juego)
	juego = carta_triunfo(mazo_sobrante)
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

def avanzar_ronda(juego):
	#Aca hay que verificar las apuestas y sumar esos puntos y reiniciamos apuestas

	juego.ronda.vuelta.reiniciar_vueltas()
	
	juego.ronda.avanzar()

	juego.primer_jugador = juego.siguiente_turno[primer_jugador] #Cambia al primer jugador de la ronda

	juego, mazo_sobrante = repartir_cartas(juego, MAZO_COMPLETO)

	if juego.ronda.numero_ronda == RONDA_FINAL:
		juego = carta_triunfo(juego, CARTA_CORAZONES)
	else:
		juego = carta_triunfo(juego, mazo_sobrante)
	return juego

def avanzar_vuelta(juego):
	"""
	Avanza la vuelta, devuelve el nuevo estado de juego.
	Preconodicion, las vueltas no deben superar al numero de rondas
	"""
	return juego.ronda.vuelta.avanzar()

def vuelta(juego):
	"""
	Recibido un estado de juego, realiza la comprobacion final de la vuelta.
	Precondicion, todas las cartas de la "vuelta" deben estar sobre la mesa
	Aclaracion: No avanza la vuelta, eso lo hace la funcion avanzar_vuelta(juego)
	"""
	jugador_ganador = determinar_ganador_mano(juego)
	juego.jugadores[jugador_ganador].sumar_bazas()
	return juego

def tirar_carta(juego, carta):
	"""
	Pone la carta en mesa del jugador, cambia turno y saca dicha carta de la mano del jugador. 
	"""
	juego.jugadores[turno_actual].mano.remove(Carta)

	#aca habria que agregar la carta en la mesa, la de cada jugador

	return juego

def limpiar_mesa(juego):
	"""
	Recibido un estado de juego, limpia la mesa (saca todas las cartas que estan en la mesa de la vuelta)
	"""
	juego.ronda.vuelta.limpiar_mesa()
	return juego

def carta_triunfo(juego, mazo):
	"""
	Recibido un estado de juego y un mazo sobrante (lista de Cartas), saca una al azar y actualiza la carta triunfo del estado de juego
	"""
	juego.ronda.vuelta.carta_triunfo(mazo)
	return juego

def pedir_apuesta(juego, apuesta):
	asignas apuesta a jugador turno actual 
	cambias turno

def carta_valida(carta):

def determinar_ganador_mano(juego):
	"""
	Recibido un estado de juego, determina quien fue el ganador de la mano.
	Devuelve el nombre del jugador.
	"""


def contabilizar_puntos_ronda(juego):
	"""
	Recibe un estado de juego.

	"""
	pass
