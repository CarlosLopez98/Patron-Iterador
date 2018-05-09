from EquipoA import EquipoA
from EquipoB import EquipoB

def main():
	argentina = EquipoA()
	colombia = EquipoB()

	seleccionar(argentina.crearIterador())
	seleccionar(colombia.crearIterador())

def seleccionar(iterador):
	while iterador.hayMas() == True:
		print iterador.siguiente()

main()
