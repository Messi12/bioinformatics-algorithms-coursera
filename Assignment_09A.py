#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Trie Construction Problem
Assignment #: 09
Problem ID: A
URL: https://stepic.org/Bioinformatics-Algorithms-2/Preprocessing-Patterns-into-a-Trie-294/step/3
'''
from scripts import Trie


def trie_edges(words):
    '''Returns the edges of a trie constructed from the given words in adjacency format.'''

    # Construct the trie.
    t = Trie(words)

    # Convert trie edges to adjacency form, as edges are currently dictionary items.
    # Converts: ((1, 2), 'A')  --> '1 2 A'
    adjacency_format = lambda item: ' '.join(map(str,item[0]))+' '+item[1]

    # Return all edges converted to adjacency form.
    return map(adjacency_format, t.edges.items())


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('data/stepic_9a.txt') as input_data:
        words = [line.strip() for line in input_data.readlines()]

    # Get the adjacency list.
    adjacency_list = trie_edges(words)

    # Print and save the answer.
    print '\n'.join(adjacency_list)
    with open('output/Assignment_09A.txt', 'w') as output_file:
        output_file.write('\n'.join(adjacency_list))

if __name__ == '__main__':
    main()
