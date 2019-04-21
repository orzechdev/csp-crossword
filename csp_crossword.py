from utils import print_title
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


class CspCrossword:
    WORD_DIRECTION_X = 0
    WORD_DIRECTION_Y = 1

    def __init__(self, size_x, size_y, ):
        self.size_x = size_x
        self.size_y = size_y
        print_title('CSP CROSSWORD: new board with size x=' + str(size_x) + ', y=' + str(size_y))
        self.board, self.board_result = self.init_board(size_x, size_y)
        print(self.board)
        print(self.board_result)

    def plot(self):
        cmap = colors.ListedColormap(['white', 'black'])

        fig, ax = plt.subplots()
        ax.matshow(self.board[0], cmap=cmap)

        # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-.5, self.board.shape[2], 1))
        ax.set_yticks(np.arange(-.5, self.board.shape[1], 1))
        ax.set_yticklabels([])
        ax.set_xticklabels([])

        for (i, j), z in np.ndenumerate(self.board_result[0]):
            ax.text(j, i, z.upper(), ha='center', va='center', size=30)

        plt.show()

    def print_result(self):
        print(self.board_result)

    def backward_assign_words(self, lemmas):
        if np.sum(self.board[1]) + np.sum(self.board[0]) == self.size_x * self.size_y:
            return True
        # print_title('CSP CROSSWORD: possible words')
        # print(lemmas)
        print_title('CSP CROSSWORD: start assigning possible words')
        for col in range(0, self.board.shape[1]):
            for row in range(0, self.board.shape[2]):
                # if self.board[0, col, row] == 0 and self.board[1, col, row] == 0:
                if self.is_needed_word_assign(row, col, self.WORD_DIRECTION_X):
                    length_x = self.get_require_word_length(row, col, self.WORD_DIRECTION_X)  # EDITED !!!!!!!!
                    if length_x > 1:
                        lemmas_x = lemmas[[length_x == len(lemma) for lemma in lemmas]]
                        for lemma_x in lemmas_x:
                            lemma_x_possible = self.is_possible_assignment(lemma_x, row, col, self.WORD_DIRECTION_X)
                            if lemma_x_possible:
                                chars_inserted_x = self.fill_board_with_word(lemma_x, row, col, self.WORD_DIRECTION_X)

                                lemma_x_index = np.where(lemmas == lemma_x)[0][0]
                                np.delete(lemmas, lemma_x_index)

                                is_next_assigned = self.backward_assign_words(lemmas)

                                if is_next_assigned:
                                    return True

                                self.remove_word_from_board(chars_inserted_x, row, col, self.WORD_DIRECTION_X)
                                np.append(lemmas, lemma_x_index)

                if self.is_needed_word_assign(row, col, self.WORD_DIRECTION_Y):
                    length_x = 0  # self.get_require_word_length(row, col, self.WORD_DIRECTION_X)  # EDITED !!!!!!!!
                    length_y = self.get_require_word_length(row, col, self.WORD_DIRECTION_Y)  # EDITED !!!!!!!!
                    if length_y > 1:

                        lemmas_y = lemmas[[length_y == len(lemma) for lemma in lemmas]]
                        for lemma_y in lemmas_y:
                            lemma_y_possible = self.is_possible_assignment(lemma_y, row, col,
                                                                           self.WORD_DIRECTION_Y)
                            if lemma_y_possible:
                                chars_inserted_y = self.fill_board_with_word(lemma_y, row, col,
                                                                             self.WORD_DIRECTION_Y)

                                lemma_y_index = np.where(lemmas == lemma_y)[0][0]
                                np.delete(lemmas, lemma_y_index)

                                is_next_assigned = self.backward_assign_words(lemmas)

                                if is_next_assigned:
                                    return True

                                self.remove_word_from_board(chars_inserted_y, row, col, self.WORD_DIRECTION_Y)
                                np.append(lemmas, lemma_y_index)

                    # else:
                    #     self.board[1, col, row] = 1
                        # really?? none return?

        print_title('CSP CROSSWORD: end assigning words')

        return False

    def remove_word_from_board(self, chars_to_remove, x, y, direction):
        for cell in range(0, chars_to_remove.shape[0]):
            if chars_to_remove[cell] != '':
                if direction == self.WORD_DIRECTION_X:
                    self.board_result[0, y, cell] = ''
                    self.board[1, y, cell] = 0
                else:
                    self.board_result[0, cell, x] = ''
                    self.board[1, cell, x] = 0

    def fill_board_with_word(self, lemma, x, y, direction):
        chars_inserted = np.empty(0, dtype=np.str)
        for cell in range(0, len(lemma)):
            cell_possible_to_fill = self.board[0, y, cell] if direction == self.WORD_DIRECTION_X else self.board[0, cell, x]
            cell_fill = self.board[1, y, cell] if direction == self.WORD_DIRECTION_X else self.board[1, cell, x]
            if cell_fill == 0 and cell_possible_to_fill == 0:
                if direction == self.WORD_DIRECTION_X:
                    self.board_result[0, y, cell] = lemma[cell]
                    self.board[1, y, cell] = 1
                    print('filled x with:' + lemma)
                else:
                    self.board_result[0, cell, x] = lemma[cell]
                    self.board[1, cell, x] = 1
                    print('filled y with:' + lemma)
                np.append(chars_inserted, lemma[cell])
            else:
                np.append(chars_inserted, '')
        return chars_inserted

    def is_possible_assignment(self, lemma_to_check, x, y, direction):
        for cell in range(0, len(lemma_to_check)):
            cell_fill = self.board[1, y, cell] if direction == self.WORD_DIRECTION_X else self.board[1, cell, x]
            cell_result = self.board_result[0, y, cell] if direction == self.WORD_DIRECTION_X else self.board_result[0, cell, x]
            print('is_possible_assignment: ', cell_fill, cell_result, direction)
            if cell_fill == 0:
                continue
            elif cell_fill == 1 and cell_result == lemma_to_check[cell]:
                continue
            print('is_possible_assignment False: ', lemma_to_check)
            return False
        print('is_possible_assignment True: ', lemma_to_check)
        return True

    def get_require_word_length(self, x, y, direction):
        board_slice = self.board[0, y, x:] if direction == self.WORD_DIRECTION_X else self.board[0, y:, x]
        length = 0
        for cell in range(0, board_slice.shape[0]):
            if board_slice[cell] == 1:
                return length
            else:
                length += 1
        return board_slice.shape[0]  # length   EDITED !!!!!!!!

    def is_needed_word_assign(self, x, y, direction):
        if direction == self.WORD_DIRECTION_X:
            is_word_beginning = (x == 0 or self.board[0, y, x - 1] == 1) and self.board[0, y, x] == 0
            is_more_than_just_letter = self.board[0, y, x:].shape[0] > 1 and self.board[0, y, x + 1] == 0
            is_required_word = is_more_than_just_letter and self.board[1, y, x + 1] == 0
            print(is_word_beginning, is_more_than_just_letter, is_required_word, x, y, 'direction: ', direction)
            if is_word_beginning and is_more_than_just_letter and is_required_word:
                return True
            else:
                return False
        else:
            is_word_beginning = (y == 0 or self.board[0, y - 1, x] == 1) and self.board[0, y, x] == 0
            is_more_than_just_letter = self.board[0, y:, x].shape[0] > 1 and self.board[0, y + 1, x] == 0
            is_required_word = is_more_than_just_letter and self.board[1, y + 1, x] == 0
            print(is_word_beginning, is_more_than_just_letter, is_required_word, x, y, 'direction: ', direction)
            if is_word_beginning and is_more_than_just_letter and is_required_word:
                return True
            else:
                return False

    # def start(self):
    #     print_title('CSP CROSSWORD: start')
    #
    #     print_title('CSP CROSSWORD: init board with size 5')
    #     board = self.init_board(5)
    #     print(board)
    #
    #     # print_title('CSP CROSSWORD: get possible values')
    #     # possible_values = get possible values...
    #     # print(possible_values)
    #
    #     print_title('CSP CROSSWORD: end')

    @staticmethod
    def init_board(size_x, size_y):
        board = np.zeros((2, size_x, size_y), dtype=np.int16)
        board_result = np.empty((1, size_x, size_y), dtype=np.str)
        # board = np.append(board_int, board_str, 0)
        board_constraint = np.empty(0)

        for i in range(1, size_x, 2):
            for j in range(1, size_y, 2):
                board[0, i, j] = 1

        return board, board_result

