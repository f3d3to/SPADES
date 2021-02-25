import gamelib

POSICION_CORRECTA, POSICION_INCORRECTA = "correcto", "incorrecto"

def click(posicion):
	"""
	Reproduce sonido que esta ingresado en la ruta posicion.wav
	"""
	gamelib.play_sound(f"sounds/{posicion}.wav")