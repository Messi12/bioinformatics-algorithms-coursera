#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Fitting Alignment Problem
Assignment #: 07
Problem ID: B
URL: https://stepic.org/Bioinformatics-Algorithms-2/The-Changing-Faces-of-Sequence-Alignment-248/step/5
'''


def fitting_alignment(v,w):
    '''Returns the fitting alignment of strings v and w.'''
    from numpy import zeros

    # Initialize the matrices.
    S = zeros((len(v)+1, len(w)+1), dtype=int)
    backtrack = zeros((len(v)+1, len(w)+1), dtype=int)

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - 1, S[i][j-1] - 1, S[i-1][j-1] + [-1, 1][v[i-1] == w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Get the position of the highest scoring cell corresponding to the end of the shorter word w.
    j = len(w)
    i = max(enumerate([S[row][j] for row in xrange(len(w), len(v))]),key=lambda x: x[1])[0] + len(w)
    max_score = str(S[i][j])

    # Initialize the aligned strings as the input strings up to the position of the high score.
    v_aligned, w_aligned = v[:i], w[:j]

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Backtrack to start of the fitting alignment.
    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut off v at the ending point of the backtrack.
    v_aligned = v_aligned[i:]

    return max_score, v_aligned, w_aligned

if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_7b.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]

    # Get the fitting alignment.
    alignment = fitting_alignment(word1, word2)

    # Print and save the answer.
    print '\n'.join(alignment)
    with open('output/Assignment_07B.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))
