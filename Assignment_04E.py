#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Eulerian Cycle Problem
Assignment #: 04
Problem ID: E
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/From-Eulers-Theorem-to-an-Algorithm-for-Finding-Eulerian-Cycles-203/#step-2
'''

import networkx as nx

# Read the input data.
with open('data/stepic_4e.txt') as input_data:
    edges = [line.strip().split(' -> ') for line in input_data.readlines()]

# Properly format the edges.
edges2 = []
for edge in edges:
    if ',' in edge[1]:
        for node in edge[1].split(','):
            edges2.append(map(int, [edge[0], node]))
    else:
        edges2.append(map(int, edge))

# Create the graph.
G = nx.DiGraph()
G.add_edges_from(edges2)

# Find an eulerian cycle.
path = [str(e[0]) for e in nx.eulerian_circuit(G)]
path.append(path[0])

# Print and save the answer.
print '->'.join(path)
with open('output/Assignment_04E.txt', 'w') as output_data:
    output_data.write('->'.join(path))
