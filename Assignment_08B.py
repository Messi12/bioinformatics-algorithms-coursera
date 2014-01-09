#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Number of Breakpoints Problem
Assignment #: 08
Problem ID: B
URL: https://stepic.org/Bioinformatics-Algorithms-2/Breakpoints-287/step/1
'''


def breakpoint_count(permutation):
    '''Returns the number of breakpoints in a given permutation.'''

    # Prepend 0 and append len(permutation)+1 to check if the endpoints are in place.
    permutation = [0] + permutation + [len(permutation)+1]

    return sum(map(lambda x,y: x - y != 1, permutation[1:], permutation[:-1]))


if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_8b.txt') as input_data:
        perm = map(int, input_data.read().strip().lstrip('(').rstrip(')').split())

    # Get the number of breakpoints
    num_of_breakpoints = breakpoint_count(perm)

    # Print and save the answer.
    print str(num_of_breakpoints)
    with open('output/Assignment_08B.txt', 'w') as output_data:
        output_data.write(str(num_of_breakpoints))
