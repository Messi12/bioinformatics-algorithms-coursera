#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Edit Distance
Assignment #: 07
Problem ID: A
URL: https://stepic.org/Bioinformatics-Algorithms-2/The-Changing-Faces-of-Sequence-Alignment-248/step/3
'''


def edit_distance(v,w):
    '''Returns the edit distance of strings v and w.'''
    from numpy import zeros

    # Initialize matrix M.
    M = zeros((len(v)+1,len(w)+1), dtype=int)
    for i in range(1,len(v)+1):
        M[i][0] = i
    for j in range(1,len(w)+1):
        M[0][j] = j

    # Compute each entry of M.
    for i in xrange(1,len(v)+1):
        for j in xrange(1,len(w)+1):
            if v[i-1] == w[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j]+1, M[i][j-1]+1, M[i-1][j-1]+1)

    # Print and save the desired edit distance.
    return M[len(v)][len(w)]

if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_7a.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]

    # Get the edit distance.
    e_dist = edit_distance(word1, word2)

    # Print and save the answer.
    print str(e_dist)
    with open('output/Assignment_07A.txt', 'w') as output_data:
        output_data.write(str(e_dist))
