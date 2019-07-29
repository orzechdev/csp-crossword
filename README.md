# Solving the crossword

* [Used technologies](#used-technologies)
* [Problem description](#problem-description)
* [How the algorithm works](#how-the-algorithm-works)
* [Results (with backtracking search)](#results-with-backtracking-search)

## Used technologies
* Python
* Numpy
* Matplotlib

## Problem description

There is a board of size: n x m fields to be used as a canvas for a crossword. A set S of all English words (or for any other natural language) can be used to select words from, but only k of them can be used in a crossword. The problem parameters are: S, n, m and k. We need to find such a way of placing words across the board that one field includes at most one letter and every continuous sequence of letters read horizontally or vertically is a word from the selected subset of the size k of S. A solution must include exactly k words from S. Some fields of the board can be left empty.

The list of English lemmas are extracted from the British National Corpus prepared by Prof. Adam Kilgarriff: https://www.kilgarriff.co.uk/bnc-readme.html . There are selected from the list only: adverbs (adv), verbs (v), adjectives (a) and nouns (n).

## How the algorithm works

The program is an example of constraint satisfaction problem. It can use either backtracking search algorithm or search with forward checking heuristic.

Example board:

![example-board](readme-files/example-board.jpg)

Board is n x m matrix

Blue – vertically,<br/>
Green – horizontally,<br/>
Red - constraint<br/>

Variables:

![variables](readme-files/variables.jpg)

Domains:

Domain contains lemmas from English language – adverbs, verbs, adjectives and nouns – selected respective for the word size i.e.:

![domain](readme-files/domain.jpg)

Constraint:

![constraint 1](readme-files/constraint-1.jpg)
![constraint 2](readme-files/constraint-2.jpg)

## Results (with backtracking search)

Board size: 2x2<br />
Time elapsed: 0.009027481079101562<br />
Result:

![backtrack result 2x2](readme-files/back-result-2-2.jpg)

Board size: 4x4<br />
Time elapsed: 0.01701951026916504<br />
Result:

![backtrack result 4x4](readme-files/back-result-4-4.jpg)

Board size: 4x6<br />
Time elapsed: 0.3980727195739746<br />
Result:

![backtrack result 4x6](readme-files/back-result-4-6.jpg)

Board size: 6x4<br />
Time elapsed: 0.04613971710205078<br />
Result:

![backtrack result 6x4](readme-files/back-result-6-4.jpg)

Board size: 6x6<br />
Time elapsed: 10.678395986557007<br />
Result:

![backtrack result 6x6](readme-files/back-result-6-6.jpg)
