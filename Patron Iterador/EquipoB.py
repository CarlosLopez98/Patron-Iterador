""" Clase AgregadoConcreto """

from Agregado import Agregado
from IteradorEquipoB import IteradorEquipoB

class EquipoB(Agregado):

	""" AGREGADO CONCRETO EL CUAL ES UN EQUIPO DE FUTBOL B """

	def __init__(self):
		super(EquipoB,self).__init__()
		self.jugadores = ()

	def getJugadores(self):
		self.jugadores = ("James","Falcao","Cuadrado","Ospina")

		return self.jugadores

	#Override
	def crearIterador(self):
		p = IteradorEquipoB(self.getJugadores())
		return p