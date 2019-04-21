from csp_crossword import CspCrossword
import numpy as np
import csv


def main():
    csp_crossword = CspCrossword(11, 4)
    # csp_crossword = CspCrossword(5, 7)
    lemmas = get_lemmas()
    csp_crossword.backward_assign_words(lemmas)
    csp_crossword.print_result()
    csp_crossword.plot()


def get_lemmas():
    lemmas = []
    with open('lemma_filtered.txt', newline='\n') as input_file:
        for row in csv.reader(input_file, delimiter="\t"):
            lemmas.append(row)
    return np.array(lemmas)[:, 2]


main()

