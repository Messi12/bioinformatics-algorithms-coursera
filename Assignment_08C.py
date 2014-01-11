#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: 2-Break Distance Problem
Assignment #: 08
Problem ID: C
URL: https://stepic.org/Bioinformatics-Algorithms-2/Computing-the-2Break-Distance-288/step/1
'''


def two_break_dist(P, Q):
    '''Returns the 2-Break Distance of Circular Chromosomes P and Q.'''

    # Construct the break point graph of P and Q.
    edges = {}
    for block in P+Q:
        L = len(block)
        # Note: Modulo L in the higher index for the edge between the last and first elements.
        for i in xrange(len(block)):
            # Add the edge between consecutive items.
            if block[i] in edges:
                edges[block[i]].append(-1*block[(i+1) % L])
            else:
                edges[block[i]] = [-1*block[(i+1) % L]]
            # Add in the reverse edge, as we aren't guaranteed a directed cycle without it.
            if -1*block[(i+1) % L] in edges:
                edges[-1*block[(i+1) % L]].append(block[i])
            else:
                edges[-1*block[(i+1) % L]] = [block[i]]

    # Count the number of cycles in the break point graph.
    cycles = 0
    while len(edges) > 0:
        cycles += 1
        current = edges.keys()[0]
        while current in edges:
            temp = edges[current][0]
            if len(edges[current]) == 1:
                del edges[current]
            else:
                edges[current] = edges[current][1:]
            # Remove the complementary edge.
            if edges[temp] == [current]:
                del edges[temp]
            else:
                edges[temp].remove(current)

            current = temp

    # Theorem: d(P,Q) = blocks(P,W) - cycles(P,Q)
    return sum([len(block) for block in P]) - cycles


if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_8c.txt') as input_data:
        P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in input_data.readlines()]
        P = [map(int, block.split()) for block in P]
        Q = [map(int, block.split()) for block in Q]

    # Get the 2-Break Distance.
    dist = two_break_dist(P, Q)

    # Print and save the answer.
    print str(dist)
    with open('output/Assignment_08C.txt', 'w') as output_data:
        output_data.write(str(dist))
