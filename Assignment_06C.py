#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Longest Common Subsequence Problem
Assignment #: 06
Problem ID: C
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Backtracking-in-the-Alignment-Graph-245/#step-5
'''


# No need for two functions, as in the problem description. I replaced the recursive function
# with a while loop in the first function.  Also, no need for the backtrack array, as all of
# that information is easily recoverable from the original array.
def longest_common_subsequence(v, w):
    '''Returns the longest longest common subsequence of strings v and w.'''
    from numpy import zeros

    # Initialize the array S and iterate through all character of v and w.
    S = zeros((len(v)+1,len(w)+1), dtype=int)
    for i in xrange(len(v)):
        for j in xrange(len(w)):
            if v[i] == w[j]:
                S[i+1][j+1] = S[i][j]+1
            else:
                S[i+1][j+1] = max(S[i+1][j],S[i][j+1])

    # Recover a maximum substring.
    longest_sseq = ''
    i,j = len(v), len(w)
    while i*j != 0:
        if S[i][j] == S[i-1][j]:
            i -= 1
        elif S[i][j] == S[i][j-1]:
            j -= 1
        else:
            longest_sseq = v[i-1] + longest_sseq
            i -= 1
            j -= 1

    return longest_sseq

if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_6c.txt') as input_data:
        dna1, dna2 = [line.strip() for line in input_data.readlines()]

    # Get the longest common subsequence.
    longest_subseq = longest_common_subsequence(dna1, dna2)

    # Print and save the answer.
    print longest_subseq
    with open('output/Assignment_06C.txt', 'w') as output_data:
        output_data.write(longest_subseq)
