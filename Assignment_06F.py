#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Local Alignment
Assignment #: 06
Problem ID: F
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/From-Global-to-Local-Alignment-247/#step-3
'''

from scripts import PAM250


def local_alignment(v, w, scoring_matrix, sigma):
    '''Returns the score and local alignment with the given scoring matrix and indel penalty sigma for strings v, w.'''
    from numpy import unravel_index, zeros

    # Initialize the matrices.
    S = zeros((len(v)+1, len(w)+1), dtype=int)
    backtrack = zeros((len(v)+1, len(w)+1), dtype=int)

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], 0]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Get the position of the highest scoring cell in the matrix and the high score.
    i,j = unravel_index(S.argmax(), S.shape)
    max_score = str(S[i][j])

    # Initialize the aligned strings as the input strings up to the position of the high score.
    v_aligned, w_aligned = v[:i], w[:j]

    # Backtrack to start of the local alignment starting at the highest scoring cell.
    while backtrack[i][j] != 3 and i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut the strings at the ending point of the backtrack.
    v_aligned = v_aligned[i:]
    w_aligned = w_aligned[j:]

    return max_score, v_aligned, w_aligned

if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_6f.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]

    # Get the local alignment (given sigma = 5 in problem statement).
    alignment = local_alignment(word1, word2, PAM250(), 5)

    # Print and save the answer.
    print '\n'.join(alignment)
    with open('output/Assignment_06F.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))
