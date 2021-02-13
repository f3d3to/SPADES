
PALOS = "D", "C", "P", "T" 
CARTAS = 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", 1

from random import randrange

class Mazo:
	def __init__(self):
		"""
		Genera un mazo con todas las cartas.
		"""
		self.cartas = []
		self.cantidad = len(CARTAS) * len(PALOS)
		for palo in PALOS:
			for numero in CARTAS:
				self.cartas.append(Carta(numero, palo))

	def sacar_carta(self):
		"""
		Saca una carta del mazo al azar y la devuelve
		"""
		carta_random = randrange(self.cantidad)
		self.cantidad -= 1
		return self.cartas.pop(carta_random)

class Jugador:
	def __init__(self, nombre):
		self.nombre = nombre
		self.mano = Mano()
		self.puntos = 0

	def limpiar_mano(self):
		"""
		Limpia la mano de cartas
		"""
		self.cartas = 0

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
		for jugador in jugadores:
			self.jugadores[jugador] = Jugador(jugador)

	def repartir(self, mazo):
		"""
		Reparte self.ronda cartas a cada jugador descontandolas del mazo recibido
		"""
		for jugador in self.jugadores:
			for i in range(self.ronda):
				jugador.mano.agregar_carta(mazo.sacar_carta())

	def siguiente_ronda(self):
		"""
		Avanza a la siguiente ronda
		"""
		self.ronda.avanzar()

class Carta:
	def __init__(self, numero, palo):
		self.palo = palo
		self.numero = numero
		self.descubierta = False
		self.triunfo = False

class Mano:
	def __init__(self):
		self.cartas = {}

	def agregar_carta(self, carta):
		"""
		Agrega una carta a la mano
		"""	

class Ronda:
	def __init__(self):
		self.ronda = 1
		self.palo = None

	def palo_ganador(self, palo):
		"""
		Recibe un palo entre CORAZONES, DIAMANTE, PICA, TREVOL y lo asigna al palo ganador 
		"""
		self.palo = palo

	def avanzar(self):
		"""
		Avanza a la siguiente ronda
		"""
		self.ronda += 1

def crear_juego(jugadores):
	"""
	Recibe una lista con cada nombre de jugador y crea y devuelve un nuevo estado de juego del tipo Juego.
	"""
	return Juego(jugadores)

def mezclar_mazo():
	"""
	Recibe un mazo ordenado y lo devuelve mezclado.
	"""

	pass

def repartir_cartas():
	"""
	Recibe un mazo.
	Devuelve un estado de juego nuevo.
	"""
	pass

def pedir_apuestas():
	"""
	"""

	pass

def determinar_ganador_mano():
	"""
	"""

def contabilizar_puntos_ronda(juego):
	"""
	Recibe un estado de juego.

	"""
	pass

def ronda_terminada():
	"""
	Recibe un estado de juego.
	Devuelve si el juego esta terminado.
	"""
	pass

def siguiente_ronda(juego):
	"""
	Recibe un estado de juego del tipo Juego.
	Avanza de ronda y devuelve el nuevo estado de juego.
	"""
	return juego.siguiente_ronda()