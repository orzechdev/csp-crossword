from csp_crossword import CspCrossword


def main():
    csp_crossword = CspCrossword(5, 7)
    csp_crossword.assign_words()
    csp_crossword.plot()


main()

