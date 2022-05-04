import modsim as ms
import pandas
from matplotlib import pyplot

from src.Functions import Functions
from src.System import MSystem

"""
ms.State: estado del sistema, cambia con la evolucion de la simul.
    bikeshare: cantidad de bicicletas en cada lado
    poblacional: la poblacion en cada instante de simulación

ms.System:
    bikeshare: cantidad de bicicletas en total, la cantidad de destinos, tasas de partida de cada lado, etc.
    poblacional: tiempo inicial, crecimiento anual, tiempo final, ...
"""

wiki = "https://en.wikipedia.org/wiki/Estimates_of_historical_world_population"

tablas = pandas.read_html(wiki, header=0, index_col=0, decimal='M')

tabla2 = tablas[2]
tabla2.columns = ['census', 'prb', 'un', 'maddison', 'hyde', 'tanton', 'biraben', 'mj', 'thomlinson', 'durand', 'clark']

census = tabla2.census / 1e9
un = tabla2.un / 1e9

t_0 = ms.get_first_label(census)
t_end = ms.get_last_label(census)
p_0 = census[t_0]
p_end = census[t_end]

system = MSystem(t_0, t_end, p_0, p_end)
function = Functions(system=system)


def plot_result_quadratic(census, un, result, title):
    pyplot.clf()
    ms.plot(result, '-', label="Modelo")
    ms.plot(census, ':', label="US censo")
    ms.plot(un, '--', label="UN censo")
    ms.decorate(title=title, xlabel='Año', ylabel='Poblacion (miles de millones)')
    ms.savefig("Population-Model.jpg")


def plot_result_net_growth(population_array, net_growth, title):
    pyplot.clf()
    ms.plot(population_array, net_growth)
    ms.decorate(title=title, xlabel="poblacion", ylabel="crecimiento neto")
    ms.savefig("NetGrowth-Model.png")


# result = function.run_simulation(function.step_quadratic)
# REEMPLAZAMOS POR LA NUEVA FUNCION:
result = function.run_simulation(function.step_quadratic_new)

plot_result_quadratic(census, un, result, "Modelo cuadratico")

# graficando el crecimiento neto
population_array = ms.linspace(0, 15, 100)
net_growth = system.alpha * population_array + system.beta * population_array ** 2
plot_result_net_growth(population_array, net_growth, "Crecimiento neto")
