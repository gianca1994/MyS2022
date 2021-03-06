import numpy as np


def grid_render(size, num_cells):
    return (size - 1) / num_cells


def make_zero_matrix(main_screen):
    return np.zeros((
        main_screen.getHorizontalCells(),
        main_screen.getVerticalCells()
    ))


def read_txt_file():
    return np.loadtxt('matrix.txt', skiprows=0)


def write_txt_file(row, column):
    zero_matrix = np.zeros((row, column))
    np.savetxt('matrix.txt', zero_matrix, '%.0f')
