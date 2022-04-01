"""
El “juego” consiste en desarrollar un patrón de figuras que evolucionen de acuerdo a reglas predeterminadas, a partir de una configuración inicial y un conjunto de reglas.

La competencia consiste en descubrir nuevas formas originales y calcular cuántas generaciones evoluciona el sistema antes de que se repitan o desaparezcan. Esto se realiza en una grilla de celdas que se estira al infinito en todas las direcciones. Este efecto lo lograremos considerando que la última columna de la derecha tenga por vecina a la primera columna de la izquierda, y lo mismo con la fila de abajo y de arriba. Una celda viva se marcará con un 1 o se pintará de un color gris oscuro, mientras que una celda muerta se marcará con un 0 o se pintará con un color blanco.

Las reglas son:

“Una celda viviente sobrevive únicamente si tiene 2 o 3 celdas vecinas vivas”. Caso contrario, muere.
“El nacimiento de una nueva celda se da si esta tiene exactamente 3 celdas vivas vecinas”
Estas simples reglas tienen un potencial asombroso de generar patrones complejos, dependiendo del patrón inicial. En todo momento el programa debe mostrar la evolución de la grilla e ir mostrando el estado del sistema, es decir, la cantidad de celdas vivas y muertas, además del número de generaciones que han pasado hasta el momento. Se debe permitir el ingreso de celdas vivas en cualquier posición de la grilla antes de comenzar el juego.

La grilla por defecto deberá tener 10 x 10.

El programa se debe detener en caso de que se hayan muerto todas las celdas.

Se le debe permitir al usuario cargar el patrón inicial y lanzar la simulación para ver cómo evoluciona el modelo.
"""
import os
import getopt
import sys
from time import sleep

import numpy as np
import pygame

from src.utilities import function


def option_reading():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'r:c:', ['rows=', 'column='])

    if len(opt) != 2:
        row, column = 10, 10

    else:
        for (op, arg) in opt:
            if op in ['-r', '--row']:
                row = int(arg)
            elif op in ['-c', '--column']:
                column = int(arg)

    assert (row, column) is not None
    return row, column


def render_screen(main_screen, size, num_cells, width_cell=False):
    main_screen.setWidthCell(
        function.grid_render(size, num_cells)
    ) if width_cell else main_screen.setHeightCell(
        function.grid_render(size, num_cells)
    )


def main():
    from src.models import main_screen
    generation_counter = 0
    row, column = option_reading()
    function.write_txt_file(row, column)

    os.system("clear")
    input('Modify the matrix.txt file with the desired automata and then press any key to continue.')

    main_screen = main_screen.MainScreen(500, 500, row, column, (255, 255, 255))

    # Generamos una matriz llena de ceros con la cantidad de columnas y filas que se eligieron
    matrix_status = function.read_txt_file()  # function.make_zero_matrix(main_screen)

    pygame.init()

    # Definimos el tamaño unitario para cada bloque en ancho y alto
    render_screen(main_screen, main_screen.width, main_screen.getHorizontalCells(), True)
    render_screen(main_screen, main_screen.height, main_screen.getVerticalCells())

    # Generamos la pantalla sobre la cual correra nuestro juego y le damos el color seleccionado
    screen = pygame.display.set_mode((
        main_screen.getHeight(),
        main_screen.getWidth()
    ))

    screen.fill(main_screen.getBackGroundColor())

    while True:

        updated_matrix_status = np.copy(matrix_status)
        screen.fill(main_screen.getBackGroundColor())

        for y in range(0, main_screen.getVerticalCells()):
            for x in range(0, main_screen.getHorizontalCells()):

                def status_bordering_blocks(position_x, position_y):
                    return matrix_status[
                        position_x % main_screen.getHorizontalCells(),
                        position_y % main_screen.getVerticalCells()
                    ]

                status_neighbors = status_bordering_blocks((x - 1), (y - 1)) + \
                                   status_bordering_blocks(x, (y - 1)) + \
                                   status_bordering_blocks((x + 1), (y - 1)) + \
                                   status_bordering_blocks((x - 1), y) + \
                                   status_bordering_blocks((x + 1), y) + \
                                   status_bordering_blocks((x - 1), (y + 1)) + \
                                   status_bordering_blocks(x, (y + 1)) + \
                                   status_bordering_blocks((x + 1), (y + 1))

                if matrix_status[x, y] == 0 and status_neighbors == 3:
                    updated_matrix_status[x, y] = 1

                elif matrix_status[x, y] == 1 and (status_neighbors < 2 or status_neighbors > 3):
                    updated_matrix_status[x, y] = 0

                polygon = [(x * main_screen.getWidthCell(),
                            y * main_screen.getHeightCell()
                            ),
                           ((x + 1) * main_screen.getWidthCell(),
                            y * main_screen.getHeightCell()
                            ),
                           ((x + 1) * main_screen.getWidthCell(),
                            (y + 1) * main_screen.getHeightCell()
                            ),
                           (x * main_screen.getWidthCell(),
                            (y + 1) * main_screen.getHeightCell()
                            )
                           ]

                pygame.draw.polygon(screen, (74, 74, 74), polygon, 1) if updated_matrix_status[x, y] == 0 \
                    else pygame.draw.polygon(screen, (74, 74, 74), polygon, 0)

        generation_counter += 1

        if updated_matrix_status.any() == np.zeros((row, column)).any() or \
                np.array_equal(matrix_status,updated_matrix_status):

            generation_counter -= 1
            sleep(2)
            pygame.display.flip()
            break

        sleep(0.35)
        matrix_status = np.copy(updated_matrix_status)
        pygame.display.flip()

    print(f'Final state of the matrix: \n{updated_matrix_status}\n')
    print(f'Total number of generations occurred: {generation_counter}')


if __name__ == '__main__':
    main()
