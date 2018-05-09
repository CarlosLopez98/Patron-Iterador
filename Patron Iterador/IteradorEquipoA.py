""" Iterador Concreto """

from Iterador import Iterador

class IteradorEquipoA(Iterador):

	def __init__(self, jugadores):
		super(IteradorEquipoA,self).__init__()
		self.pos = 0
		self.jugadores = jugadores
	#Override
	def primero(self):
		self.pos = 0
		jugador = self.jugadores[self.pos]
		return jugador

	#Override
	def siguiente(self):
		jugador = self.jugadores[self.pos]
		self.pos += 1
		return jugador

	#Override
	def hayMas(self):
		return self.pos+1 <= len(self.jugadores)

	#Override
	def elementoActual(self):
		return self.jugadores[self.pos]