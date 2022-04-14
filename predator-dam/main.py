import getopt
import sys

import modsim as ms

from src.models.dam import Dam
from src.models.predator import Predator
from src.models.terrain import Terrain

damM = Dam()
predatorM = Predator()
terrainM = Terrain()
DELTA_T = 1


def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'd:p:c:w:', ['dam=', 'predator=', 'capacity=', 'week='])

    for (op, arg) in opt:
        if op in ['-d', '--dam']:
            damM.setAmount(int(arg))
        elif op in ['-p', '--predator']:
            predatorM.setAmount(int(arg))
        elif op in ['-c', '--capacity']:
            terrainM.setMaximumCap(int(arg))
        elif op in ['-w', '--week']:
            terrainM.setWeek(int(arg))


def main():
    option_reading()

    # Posibles encuentros
    possible_meetings = damM.getAmount() * predatorM.getAmount()

    # Probabilidad de que un depredador nazca
    predators_born = (predatorM.getMortalityRate() * 10) / possible_meetings

    # Probabilidad de que muera una presa
    dam_dies = predatorM.getAmount() / possible_meetings

    dis_predator = predatorM.getMortalityRate() * predatorM.getAmount()

    list_live_predator = list()
    list_live_dam = list()

    # -------------------------------- Inicio del Loop --------------------------------

    # Seteo de la capacidad del terreno actual
    for i in range(terrainM.getWeek() + 1):
        terrainM.setCurrentCap(
            damM.getAmount()
        )

        inc_dam = (terrainM.getCurrentCap() / terrainM.getMaximumCap()) * damM.getBirthRate() * damM.getAmount()

        hunting = predatorM.getAmount() * damM.getAmount()

        damM.setAmount(
            damM.getAmount() + DELTA_T * (inc_dam - dam_dies * hunting)
        )

        predatorM.setAmount(
            predatorM.getAmount() + DELTA_T * (predators_born * hunting - dis_predator)
        )

        list_live_predator.append(predatorM.getAmount())
        list_live_dam.append(damM.getAmount())

    ms.plot(list_live_predator, ':', color='blue', label='Live Predators')
    ms.plot(list_live_dam, '--', color='red', label='Live Dams')

    ms.decorate(xlabel='Weeks',
                ylabel='Live Quantity',
                title='Predator vs Dam')

    ms.savefig('.\PredatorVsDam-Model.jpg')


if __name__ == '__main__':
    main()
