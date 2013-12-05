#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Approximate Pattern Matching Problem
Assignment #: 01
Problem ID: F
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Elusive-than-Others-9/#step-3
'''

with open('data/stepic_1f.txt') as input_data:
	pattern, dna, n = [line.strip() if index != 2 else int(line.strip()) for index, line in enumerate(input_data.readlines())]

approx_match = []
for i in xrange(len(dna)-len(pattern)+1):
	mismatch_count = 0
	for j in xrange(len(pattern)):
		if dna[i:i+len(pattern)][j] != pattern[j]:
			mismatch_count += 1
	
	if mismatch_count <= n:
		approx_match.append(str(i))

print ' '.join(approx_match)
with open('output/Assignment_01F.txt', 'w') as output_data:
	output_data.write(' '.join(approx_match))
