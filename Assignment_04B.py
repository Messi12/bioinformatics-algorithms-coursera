#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Overlap Graph Problem
Assignment #: 04
Problem ID: B
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/String-Reconstruction-as-a-Walk-Through-the-Overlap-Graph-198/#step-7
'''

with open('data/stepic_4b.txt') as input_data:
    dna = [line.strip() for line in input_data.readlines()]

# Lambda functions to check for overlap and print overlaps in the desired way.
check_overlap = lambda pair: pair[0][1:] == pair[1][:-1]
print_overlap = lambda pair: ' -> '.join(pair)

# Get all pairs, filter out non-overlapping pairs, print overlapping pairs appropriately.
pairs = ([dna1, dna2] for i, dna1 in enumerate(dna) for j, dna2 in enumerate(dna) if i != j)
overlaps = map(print_overlap, filter(check_overlap, pairs))

# Print and save the answer.
print '\n'.join(overlaps)
with open('output/Assignment_04B.txt', 'w') as output_data:
    output_data.write('\n'.join(overlaps))
