#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Universal String Problem
Assignment #: 05
Problem ID: C
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/From-Eulers-Theorem-to-an-Algorithm-for-Finding-Eulerian-Cycles-203/#step-8
'''

from Assignment_04E import eulerian_cycle
from itertools import product

# Read the input data.
with open('data/stepic_5c.txt') as input_data:
    k = int(input_data.read().strip())

# Create the edges.
universal_dict = {}
for kmer in [''.join(item) for item in product('01', repeat=k)]:
    if kmer[:-1] in universal_dict:
        universal_dict[kmer[:-1]].append(kmer[1:])
    else:
        universal_dict[kmer[:-1]] = [kmer[1:]]

# Get the cycle, remove the repeated last entry for the associated path.
path = eulerian_cycle(universal_dict)

# Print and save the answer.
print ''.join([item[0] for item in path[:-1]])
with open('output/Assignment_05C.txt', 'w') as output_data:
    output_data.write(''.join([item[0] for item in path[:-1]]))
