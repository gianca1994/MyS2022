import getopt
import sys

from src.models.dam import Dam
from src.models.predator import Predator
from src.models.terrain import Terrain

damM = Dam()
predatorM = Predator()
terrainM = Terrain()
deltaT = 1

def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'd:p:c:', ['dam=', 'predator=', 'capacity='])

    for (op, arg) in opt:
        if op in ['-d', '--dam']:
            damM.setAmount(int(arg))
        elif op in ['-p', '--predator']:
            predatorM.setAmount(int(arg))
        elif op in ['-c', '--capacity']:
            terrainM.setMaximumCap(int(arg))
        # elif -> Cantidad de Semanas? SI


def main():
    option_reading()

    print(f'Variables iniciales: [Presas: {damM.getAmount()} | Depredadores: {predatorM.getAmount()} | Terreno: {terrainM.getMaximumCap()}]')

    # Posibles encuentros
    possible_meetings = damM.getAmount() * predatorM.getAmount()

    # Probabilidad de que un depredador nazca
    predators_born = (predatorM.getMortalityRate() * 10) / possible_meetings

    # Probabilidad de que muera una presa
    dam_dies = predatorM.getAmount() / possible_meetings

    # -------------------------------- Inicio del Loop --------------------------------

    # Seteo de la capacidad del terreno actual
    terrainM.setCurrentCap(
        damM.getAmount()
    )

    inc_dam = (terrainM.getCurrentCap() / terrainM.getMaximumCap()) * damM.getBirthRate() * damM.getAmount()

    dis_predator = predatorM.getMortalityRate() * predatorM.getAmount()

    hunting = predatorM.getAmount() * damM.getAmount()

    damM.setAmount(
        damM.getAmount() + deltaT * (inc_dam - dam_dies * hunting)
    )

    predatorM.setAmount(
        predatorM.getAmount() + deltaT * (predators_born * hunting - dis_predator)
    )

    print(f'Depredadores que viven si hay presas: {predators_born} | Presas que mueren: {dam_dies}')
    print(f'Capacidad actual del terreno: {terrainM.getCurrentCap()}')
    print(f'inc_dam: {inc_dam}, dis_predator: {dis_predator}, hunting: {hunting}')


if __name__ == '__main__':
    main()
