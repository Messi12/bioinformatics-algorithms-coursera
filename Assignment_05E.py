#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Contig Generation Problem
Assignment #: 05
Problem ID: E
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Epilogue-Genome-Assembly-Faces-Additional-Practical-Hurdles-205/#step-5
'''

from compiler.ast import flatten

# Read the input data.
with open('data/stepic_5e.txt') as input_data:
    kmers = [line.strip() for line in input_data.readlines()]

# Construct a dictionary of edges.
edges = {}
for kmer in kmers:
    if kmer[:-1] in edges:
        edges[kmer[:-1]].append(kmer[1:])
    else:
        edges[kmer[:-1]] = [kmer[1:]]

# Determine the balanced and unbalanced edges.
balanced, unbalanced = [], []
out_values = reduce(lambda a,b: a+b, edges.values())
for node in set(out_values+edges.keys()):
    out_value = out_values.count(node)
    if node in edges:
        in_value = len(edges[node])
    else:
        in_value = 0

    if in_value == out_value == 1:
        balanced.append(node)
    else:
        unbalanced.append(node)

# Generate the contigs.
get_contigs = lambda s, c: flatten([c+e[-1] if e not in balanced else get_contigs(e,c+e[-1]) for e in edges[s]])
contigs = sorted(flatten([get_contigs(start,start) for start in set(unbalanced) & set(edges.keys())]))

# Print and save the answer.
print '\n'.join(contigs)
with open('output/Assignment_05E.txt', 'w') as output_data:
    output_data.write('\n'.join(contigs))
