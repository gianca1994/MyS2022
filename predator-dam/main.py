import getopt
import sys

from src.models.dam import Dam
from src.models.predator import Predator
from src.models.terrain import Terrain

damModel = Dam()
predatorModel = Predator()
terrainModel = Terrain()


def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'd:p:', ['dam=', 'predator='])

    for (op, arg) in opt:
        if op in ['-d', '--dam']:
            damModel.setAmount(int(arg))
        elif op in ['-p', '--predator']:
            predatorModel.setAmount(int(arg))


def main():
    option_reading()

    # Seteo de la capacidad del terreno actual
    terrainModel.setCurrentCapacity(
        damModel.getAmount() + predatorModel.getAmount()
    )

    # Posibles encuentros
    possible_meetings = damModel.getAmount() * predatorModel.getAmount()

    # Probabilidad de que un depredador nazca
    predators_born = (predatorModel.getMortalityRate() * 10) / possible_meetings

    # Probabilidad de que muera una presa
    dam_dies = predatorModel.getAmount() / possible_meetings

    print(f'Depredadores que viven si hay liebres: {predators_born} | Presas que mueren: {dam_dies}')
    print(f'Capacidad actual del terreno: {terrainModel.getCurrentCapacity()}')


if __name__ == '__main__':
    main()
