#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Longest Shared Repeat Problem
Assignment #: 09
Problem ID: E
URL: https://stepic.org/Bioinformatics-Algorithms-2/Suffix-Trees-296/step/5
'''


def main():
    '''Solves problem Problem 9E.'''
    from scripts import GeneralizedSuffixTree

    # Read the input data.
    with open('data/stepic_9e.txt') as input_data:
        text = [line.strip() for line in input_data.readlines()]

    # Construct the generalized suffix tree for the input text.
    gst = GeneralizedSuffixTree(text)

    # Find all nodes that are traversed by all words in text, meaning that the substring up to that node is in all words in text.
    candidate_nodes = filter(lambda i: len(gst.nodes[i].words) == len(text), xrange(len(gst.nodes)))

    # Get the deepest node of from the candidate nodes, where depth corresponds to substring length.
    deepest_node = max(candidate_nodes, key=lambda i: gst.node_depth(i))

    # Get the substring corresponding to a traversal up to the deepest node.
    longest_shared_repeat = gst.word_up_to_node(deepest_node)

    # Print and save the answer.
    print longest_shared_repeat
    with open('output/Assignment_09E.txt', 'w') as output_data:
        output_data.write(longest_shared_repeat)

if __name__ == '__main__':
    main()
