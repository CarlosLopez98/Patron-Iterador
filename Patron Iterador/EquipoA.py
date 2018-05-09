""" Clase AgregadoConcreto """

from Agregado import Agregado
from IteradorEquipoA import IteradorEquipoA

class EquipoA(Agregado):

	""" AGREGADO CONCRETO EL CUAL ES UN EQUIPO DE FUTBOL A """

	def __init__(self):
		super(EquipoA,self).__init__()
		self.jugadores = []

	def getJugadores(self):
		self.jugadores.append("Romero")
		self.jugadores.append("Messi")
		self.jugadores.append("Di Maria")

		return self.jugadores

	#Override
	def crearIterador(self):
		p = IteradorEquipoA(self.getJugadores())
		return p