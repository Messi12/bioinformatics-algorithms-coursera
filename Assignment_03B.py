#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Median String Problem
Assignment #: 03
Problem ID: B
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/From-Motif-Finding-to-Finding-a-Median-String-158/#step-7
'''

from itertools import product
from scripts import HammingDistance

def motif_score(pattern, motif):
	'''Returns the score of d(pattern, motif).'''
	return min([HammingDistance(motif[i:i+len(pattern)], pattern) for i in range(len(motif)-len(pattern)+1)])

with open('data/stepic_3b.txt') as input_data:
	k = int(input_data.readline())
	dna_list = [line.strip() for line in input_data.readlines()]

# Initialize the best pattern score as one greater than the maximum possible score.
best_pattern = [k*len(dna_list) + 1, None]

# Check the scores of all k-mers.
for pattern in product('ACGT', repeat=k):
	current_score = sum([motif_score(''.join(pattern),dna) for dna in dna_list])
	if current_score < best_pattern[0]:
		best_pattern = [current_score, ''.join(pattern)]

# Print and save the answer.
print best_pattern[1]
with open('output/Assignment_03B.txt', 'w') as output_data:
	output_data.write(best_pattern[1])
