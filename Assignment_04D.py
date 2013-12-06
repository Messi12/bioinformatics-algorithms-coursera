#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: De Bruijn Graph from k-mers Problem
Assignment #: 4
Problem ID: D
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Another-Walk-200/#step-7
'''

# Read the input data.
with open('data/stepic_4d.txt') as input_data:
    kmers = [line.strip() for line in input_data.readlines()]

# Create a dictionary matching (k-1)-mers to their followers.
de_bruijn_dict = dict()
for kmer in kmers:
    if kmer[:-1] in de_bruijn_dict:
        de_bruijn_dict[kmer[:-1]].add(kmer[1:])
    else:
        de_bruijn_dict[kmer[:-1]] = {kmer[1:]}

# Write the De Bruijn Graph in the specified format
de_buijn = [' -> '.join([item[0], ','.join(item[1])]) for item in de_bruijn_dict.items()]

# Print and save the answer.
print '\n'.join(de_buijn)
with open('output/Assignment_04D.txt', 'w') as output_data:
    output_data.write('\n'.join(de_buijn))
