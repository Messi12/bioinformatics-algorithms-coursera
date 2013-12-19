#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Manhattan Tourist
Assignment #: 06
Problem ID: B
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/The-Manhattan-Tourist-Problem-Revisited-261/#step-8
'''


def manhattan_tourist(n, m, down, right):
    '''Returns the longest path from (0,0) to (n,m) using the taxicab metric and weights down, right.'''
    from numpy import zeros

    # Initialize as the zero matrix.
    S = zeros((n+1,m+1), dtype=int)

    # Compute the first row and column.
    for i in xrange(1,n+1):
        S[i][0] = S[i-1][0] + down[i-1][0]
    for j in xrange(1, m+1):
        S[0][j] = S[0][j-1] + right[0][j-1]

    # Compute the interior values.
    for i in xrange(1,n+1):
        for j in xrange(1,m+1):
            S[i][j] = max(S[i-1][j]+down[i-1][j], S[i][j-1] + right[i][j-1])

    return S[n][m]

if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_6b.txt') as input_data:
        n, m = [int(input_data.readline()) for repeat in xrange(2)]
        down, right = [[map(int, row.split()) for row in matrix.split('\n')] for matrix in input_data.read().strip().split('\n-\n')]

    # Get the maximum distance.
    max_dist = str(manhattan_tourist(n, m, down, right))

    # Print and save the answer.
    print max_dist
    with open('output/Assignment_06B.txt', 'w') as output_data:
        output_data.write(max_dist)
