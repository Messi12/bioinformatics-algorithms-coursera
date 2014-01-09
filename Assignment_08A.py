#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Greedy Sorting
Assignment #: 08
Problem ID: A
URL: https://stepic.org/Bioinformatics-Algorithms-2/A-Greedy-Algorithm-for-Sorting-by-Reversals-286/step/2
'''


def greedy_sorting(permutation):
    '''A greedy algorithm to sort by reversals.'''
    from operator import neg

    # Initialize the transformation list, which stores all intermediate transformations.
    transformation_list = []

    # Quick lambda functions to find the index of a given element, and swap and negate a region in the permutation.
    k_index = lambda perm, k: map(abs, perm).index(k)
    k_sort = lambda perm, i, j: perm[:i] + map(neg, perm[i:j+1][::-1]) + perm[j+1:]

    # Loop over the permutation to sort it.
    i = 0
    while i < len(permutation):
        if permutation[i] == i+1:
            i += 1
        elif permutation[i] == -(i+1):
            permutation = k_sort(permutation, i, i)
            transformation_list.append(permutation)
        else:
            permutation = k_sort(permutation, i, k_index(permutation, i+1))
            transformation_list.append(permutation)

    # Note: the approximate reversal distance is the length of the transformation list.
    return transformation_list


if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_8a.txt') as input_data:
        perm = map(int, input_data.read().strip().lstrip('(').rstrip(')').split())

    # Get the list of recerals necessary to sort the given permutation.
    reversal_list = greedy_sorting(perm)
    # Write the permutation in the desired form for in the desired output form for stepic.
    reversal_list = ['('+' '.join([['', '+'][value > 0] + str(value) for value in perm])+')' for perm in reversal_list]

    # Print and save the answer.
    print '\n'.join(reversal_list)
    with open('output/Assignment_08A.txt', 'w') as output_data:
        output_data.write('\n'.join(reversal_list))
