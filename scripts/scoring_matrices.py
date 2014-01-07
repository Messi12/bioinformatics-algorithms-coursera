#!/usr/bin/env python
'''A Bioinformatics Algorithms script containing scoring matrices.'''


class BLOSUM62(object):
    """The BLOSUM62 scoring matrix class."""

    def __init__(self):
        """Initialize the scoring matrix."""
        import os

        with open(os.path.join(os.path.dirname(__file__), 'data/BLOSUM62.txt')) as input_data:
            items = [line.strip().split() for line in input_data.readlines()]
            self.scoring_matrix = {(item[0], item[1]):int(item[2]) for item in items}

    def __getitem__(self, pair):
        """Returns the score of the given pair of protein."""
        return self.scoring_matrix[pair[0], pair[1]]


class PAM250(object):
    """The PAM250 scoring matrix class."""

    def __init__(self):
        """Initialize the scoring matrix."""
        import os
        import pandas as pd
        # Convert the scoring matrix text file to a data frame.
        self.scoring_matrix = pd.read_table(os.path.join(os.path.dirname(__file__), 'data/PAM250.txt'), sep='  ')

    def __getitem__(self, pair):
        """Returns the score of the given pair of protein."""
        return self.scoring_matrix[pair[0]][pair[1]]
