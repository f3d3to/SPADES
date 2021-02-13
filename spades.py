
PALOS = "D", "C", "P", "T" 
CARTAS = 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", 1

from random import randrange

class Jugador:
	def __init__(self, nombre):
		self.nombre = nombre
		self.mano = []
		self.puntos = 0
		self.apuesta = 0
		self.bazas = 0
		
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
		return self.mano.remove(carta)

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
		self.jugadores = []
		#hacer diccionario con siguiente turno
		primer_jugador = jugadores[randrange(len(jugadores)-1)]
		self.turno_actual = self.primer_jugador = primer_jugador
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
		primer_jugador = siguiente_turno[primer_jugador]
		self.ronda.avanzar()

class Carta:
	def __init__(self, numero, palo):
		self.palo = palo
		self.numero = numero
		
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

def tirar_carta(juego, carta):
	"""
	Recibido un esto de juego y una carta, tira la carta en la mesa 
	"""
	
		
		
def crear_juego(jugadores):
	"""
	Recibe una lista con cada nombre de jugador y crea y devuelve un nuevo estado de juego del tipo Juego.
	"""
	return Juego(jugadores)

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
