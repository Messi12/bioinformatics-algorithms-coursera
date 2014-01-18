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


def main():
    '''Solves problem Problem 9D.'''
    from scripts import GeneralizedSuffixTree

    # Read the input data.
    with open('data/stepic_9d.txt') as input_data:
        text = input_data.read().strip()

    # Most of the workd is done by the generalized suffix tree script.
    gst = GeneralizedSuffixTree(text)

    # Get a list of all edges from the generalized suffix tree.
    edges = [gst.edge_word(e) for e in gst.edges.values()]

    # Put the edges in the proper format (i.e. want endings $0 to be $).
    # Note: This is necessary because we're using a generalized suffix tree, which uses
    # $X as the out of alphabet suffixes in order to distinguish between multiple words.
    edges = [e[:-1] if '$' in e else e for e in edges]

    # Print and save the answer.
    print '\n'.join(edges)
    with open('output/Assignment_09D.txt', 'w') as output_data:
        output_data.write('\n'.join(edges))

if __name__ == '__main__':
    main()
