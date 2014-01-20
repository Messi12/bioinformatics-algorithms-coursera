#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Shortest Non-Shared Substring Problem
Assignment #: 09
Problem ID: F
URL: https://stepic.org/Bioinformatics-Algorithms-2/Suffix-Trees-296/step/6
'''
from scripts import GeneralizedSuffixTree


def shortest_nonshared_substring(string_list):
    '''Returns the shortest nonshared substring unique to the first word in string_list.'''

    # Construct the generalized suffix tree for the input text.
    gst = GeneralizedSuffixTree(string_list)

    # Find all nodes that are traversed only by the first word in text, meaning that the substring up to that node is only in the first word.
    candidate_nodes = filter(lambda i: gst.nodes[i].words == {0}, xrange(len(gst.nodes)))

    # Filter out all nodes corresponding to the out of alphabet character unique to first word, as these are trivally only traveresed by the first word.
    # If the out of alphabet character is the only character on the edge, then its parent must be traversed by another word.
    candidate_nodes = filter(lambda i: gst.edge_word(gst.edges[gst.nodes[i].parent,i]) != '$0', candidate_nodes)

    # To get the shortest substring, only take the first character of the last edge, hence the substring has length parent_length + 1.
    shortest = min(candidate_nodes, key=lambda i: gst.node_depth(gst.nodes[i].parent)+1)

    # Shortest nonshared substring is the substring up to the first character of the edge leading to the optimal node.
    return gst.word_up_to_node(gst.nodes[shortest].parent) + gst.edge_word(gst.edges[gst.nodes[shortest].parent,shortest])[0]


def main():
    '''Solves problem Problem 9F.'''

    # Read the input data.
    with open('data/stepic_9f.txt') as input_data:
        text = [line.strip() for line in input_data.readlines()]

    # Get the shortest nonshared substring unique to the first word.
    minimal_unique_substring = shortest_nonshared_substring(text)

    # Print and save the answer.
    print minimal_unique_substring
    with open('output/Assignment_09F.txt', 'w') as output_data:
        output_data.write(minimal_unique_substring)

if __name__ == '__main__':
    main()
