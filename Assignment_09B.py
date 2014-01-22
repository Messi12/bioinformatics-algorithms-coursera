#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Multiple Pattern Matching Problem
Assignment #: 09
Problem ID: B
URL: https://stepic.org/Bioinformatics-Algorithms-2/Preprocessing-Patterns-into-a-Trie-294/step/6
'''

from scripts import Trie


def trie_pattern_matching(word, patterns):
    '''Returns the starting index off all locations in word where a string in patterns is a substring.'''

    # Construct a trie from all of the given patterns.
    t = Trie(patterns)

    # Checck each index in the word (until the remainder is shorter than the shortest pattern)
    # to see if a pattern occurs starting at the specified index.
    check_patterns = [i for i in xrange(len(word)-min(map(len, patterns))+1) if t.prefix_in_trie(word[i:]) is True]

    return check_patterns


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/stepic_9b.txt') as input_data:
        word = input_data.readline().strip()
        patterns = [line.strip() for line in input_data.readlines()]

    # Get the matching pattern indices.
    pattern_indices = trie_pattern_matching(word, patterns)

    # Print and save the answer.
    print ' '.join(map(str, pattern_indices))
    with open('output/Assignment_09B.txt', 'w') as output_data:
        output_data.write(' '.join(map(str, pattern_indices)))

if __name__ == '__main__':
    main()
