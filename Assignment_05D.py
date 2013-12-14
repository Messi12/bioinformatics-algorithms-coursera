#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: String Construction from Read-Pairs Problem
Assignment #: 05
Problem ID: D
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Assembling-Read-Pairs-204/#step-14
'''

from Assignment_05A import eulerian_path

# Read the input data.
with open('data/stepic_5d.txt') as input_data:
    d = int(input_data.readline())
    paired_reads = [line.strip().split('|') for line in input_data.readlines()]
    k = len(paired_reads[0][0])

# Construct a dictionary of edges from the paired reads.
paired_dict = {}
for pair in paired_reads:
    if (pair[0][:-1],pair[1][:-1]) in paired_dict:
        paired_dict[(pair[0][:-1],pair[1][:-1])].append((pair[0][1:],pair[1][1:]))
    else:
        paired_dict[(pair[0][:-1],pair[1][:-1])] = [(pair[0][1:],pair[1][1:])]

# Get an eulerian path from the paired edges.
paired_path = eulerian_path(paired_dict)

# Recombine the paths, accounting for their overlaps.
strings = [paired_path[0][i] + ''.join(map(lambda x: x[i][-1], paired_path[1:])) for i in xrange(2)]
text = strings[0][:k+d]+strings[1]

# Print and save the answer.
print text
with open('output/Assignment_05D.txt', 'w') as output_data:
    output_data.write(text)
