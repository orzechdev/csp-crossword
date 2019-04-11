from utils import print_title
import numpy as np


possible_values_size = 5


def start():
    print_title('CSP CROSSWORD: start')

    print_title('CSP CROSSWORD: init square with size 5')
    # square = init_square(5)
    # print(square)
    #
    # print_title('CSP CROSSWORD: get possible values')
    # possible_values = get possible values...
    # print(possible_values)

    print_title('CSP CROSSWORD: end')


def init_board(size):
    square = np.zeros((size, size), dtype=np.int16)

    return square

