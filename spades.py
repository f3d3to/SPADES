DIAMANTE, CORAZONES, PICA, TREVOL = "diamante", "corazones", "pica", "trevol"

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

	def recibir_carta(self, carta):
		"""
		Recibe una carta del tipo Carta y la suma a su mano
		"""
		self.mano.agregar_carta(carta)

	def sumar_puntos(self, puntos):
		"""
		Recibe puntos (int) y los suma
		"""
		self.puntos += puntos

class Juego:
	def __init__(self, jugadores):
		"""
		Recibe una lista jugadores, y le da los siguientes atributos:
		Crea un atributo self.ronda del objeto tipo Ronda
		Crea un atributo self.jugadores el cual es un diccionario con clave 
		"""
		self.ronda = Ronda()
		self.jugadores = {}
		for jugador in jugadores:
			self.jugadores[jugador] = Jugador(jugador)

	def repartir(self):
		"""
		Reparte self.ronda cartas a cada jugador
		"""
		for jugador in self.jugadores:
			jugador.


	def siguiente_ronda(self):
		"""
		Avanza a la siguiente ronda
		"""
		self.ronda.avanzar()

class Carta:
	def __init__(self, numero, palo):
		self.palo = palo
		self.numero = numero

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

def siguiente_ronda(juego):
	"""
	Recibe un estado de juego del tipo Juego
	Avanza de ronda y devuelve el nuevo estado de juego
	"""
	return juego.siguiente_ronda()
