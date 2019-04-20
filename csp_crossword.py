from utils import print_title
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


class CspCrossword:
    def __init__(self, size_x, size_y, ):
        self.size_x = size_x
        self.size_y = size_y
        print_title('CSP CROSSWORD: new board with size x=' + str(size_x) + ', y=' + str(size_y))
        self.square = self.init_board(size_x, size_y)
        print(self.square)

    def plot(self):
        cmap = colors.ListedColormap(['white', 'black'])

        data = np.random.rand(10, 10) * 20

        fig, ax = plt.subplots()
        ax.imshow(self.square[0], cmap=cmap)

        # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-.5, self.square.shape[2], 1))
        ax.set_yticks(np.arange(-.5, self.square.shape[1], 1))
        ax.set_yticklabels([])
        ax.set_xticklabels([])

        plt.show()

    def assign_words(self):
        print_title('CSP CROSSWORD: start assigning words')
        pass
        print_title('CSP CROSSWORD: end assigning words')

    def start(self):
        print_title('CSP CROSSWORD: start')

        print_title('CSP CROSSWORD: init board with size 5')
        square = self.init_board(5)
        print(square)

        # print_title('CSP CROSSWORD: get possible values')
        # possible_values = get possible values...
        # print(possible_values)

        print_title('CSP CROSSWORD: end')

    @staticmethod
    def init_board(size_x, size_y):
        square = np.zeros((2, size_x, size_y), dtype=np.int16)

        for i in range(1, size_x, 2):
            for j in range(1, size_y, 2):
                square[0, i, j] = 1

        return square

