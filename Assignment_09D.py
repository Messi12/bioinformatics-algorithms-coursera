#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Suffix Tree Construction Problem
Assignment #: 09
Problem ID: D
URL: https://stepic.org/Bioinformatics-Algorithms-2/Suffix-Trees-296/step/4
'''
from scripts import GeneralizedSuffixTree


def suffix_tree_edges(word):
    '''Returns the edge subsrings associated with the suffix tree for the given word.'''

    # Most of the work is done by the generalized suffix tree script (see scripts folder).
    gst = GeneralizedSuffixTree(word)

    # Get a list of all edge substrings from the generalized suffix tree.
    edges = [gst.edge_word(e) for e in gst.edges.values()]

    # Return the edges in suffix tree format (i.e. want endings $0 to be $).
    # Note: This is necessary because we're using a generalized suffix tree, which uses $0, $1, ..., $N
    # as the out of alphabet suffixes in order to distinguish between word 0, word 1, ..., word N.
    return [e[:-1] if '$' in e else e for e in edges]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('data/stepic_9d.txt') as input_data:
        text = input_data.read().strip()

    # Get the edge substrings.
    edge_substrings = suffix_tree_edges(text)

    # Print and save the answer.
    print '\n'.join(edge_substrings)
    with open('output/Assignment_09D.txt', 'w') as output_data:
        output_data.write('\n'.join(edge_substrings))

if __name__ == '__main__':
    main()
