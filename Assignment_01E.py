#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Minimum Skew Problem
Assignment #: 01
Problem ID: E
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Peculiar-Statistics-of-the-Forward-and-Reverse-Half-Strands-7/#step-6
'''

with open('data/stepic_1e.txt') as input_data:
	dna = input_data.read().strip()

skew_value, min_skew, min_ind = 0, 1, []
for index, nucleotide in enumerate(dna):
	# Determine the skew value.
	if nucleotide == 'C':
		skew_value -= 1
	elif nucleotide == 'G':
		skew_value += 1
	# Check if it matches the current minimum, or is a new minimum.
	if skew_value == min_skew:
		min_ind.append(str(index+1))
	elif skew_value < min_skew:
		min_skew = skew_value
		min_ind = [str(index+1)]

print ' '.join(min_ind)
with open('output/Assignment_01E.txt', 'w') as output_data:
	output_data.write(' '.join(min_ind))
