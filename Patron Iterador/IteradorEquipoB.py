""" Iterador Concreto """

from Iterador import Iterador

class IteradorEquipoB(Iterador):

	def __init__(self, jugadores):
		super(IteradorEquipoB,self).__init__()
		self.pos = 0
		self.jugadores = jugadores

	#Override
	def siguiente(self):
		jugador = self.jugadores[self.pos]
		self.pos += 1
		return jugador

	#Override
	def hayMas(self):
		return self.pos+1 <= len(self.jugadores)