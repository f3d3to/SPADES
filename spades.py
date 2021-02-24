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
		self.apuesta = -1
		self.bazas = 0
		self.carta_tirada = None
		
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
		for i_jugador in range(jugadores): #Creo un diccionario con los siguientes turnos de cada jugador
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
				jugador.mano.agregar_carta(carta_sacada)
		return mazo

	def siguiente_ronda(self):
		"""
		Avanza a la siguiente ronda, devuelve el estado de juego.
		"""
		self.primer_jugador = self.siguiente_turno[primer_jugador]
		self.ronda.avanzar()
		return juego

class Carta:
	def __init__(self, numero, palo):
		"""
		Recibe numero entero y palo en formato str
		"""
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
		self.carta_mesa = None
		self.ganador_vuelta = None
		self.numero_vuelta = 0
		self.cartas_puestas = {}

	def agregar_carta_mesa(self, carta, jugador):
		"""
		Agrega una carta a la mesa, al diccionaro cartas_puestas, donde usa a la carta como clave y valor al jugador. Si el diccionario esta vacio (la carta tirada es la primera de la mesa) se agrega a self.carta_mesa
		No devuelve nada
		"""
		if self.cartas_puestas == {}:
			self.carta_mesa = carta
		self.cartas_puestas[jugador] = carta

	def avanzar_vuelta(self):
		"""
		Avanza el numero de vuelta, reinicia todas las cartas_puestas en la mesa
		No devuelve nada
		"""
		self.numero_vuelta += 1
		self.cartas_puestas = {}
		self.carta_mesa = None

	def reiniciar_vueltas(self):
		"""
		Reinicia las vueltas a 0. (porque se cambio de ronda). Quita la carta mesa.
		"""
		self.numero_vuelta = 0
		self.carta_mesa = None


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
	juego = verificar_puntuaciones(juego)
	juego = quitar_apuestas(juego)

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
	Precondicion: la carta debe estar en la mano del jugador del turno actual. 
	"""
	turno = juego.turno_actual
	juego.jugadores[turno].mano.remove(carta)
	juego.vuelta.agregar_carta_mesa(carta, turno)
	return juego

def carta_triunfo(juego, mazo):
	"""
	Recibido un estado de juego y un mazo sobrante (lista de Cartas), saca una al azar y actualiza la carta triunfo del estado de juego
	"""
	juego.ronda.vuelta.carta_triunfo(mazo)
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

def carta_valida(juego, carta):
	"""
	Recibido un estado de juego y una carta, devuelve True si la carta es valida para tirar, False si no lo es.
	"""
	if juego.turno_actual == juego.primer_jugador:
		

def es_mayor(juego, carta1, carta2):
	"""
	Recibido un estado de juego y dos cartas las compara, si carta1 es mayor a carta2 devuelve True, sino devuelve False
	"""
	

	return carta_mayor

def determinar_ganador_mano(juego):
	"""
	Recibido un estado de juego, determina quien fue el ganador de la mano.
	Devuelve el nombre del jugador.
	"""

