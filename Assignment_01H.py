#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Frequent Words with Mismatches and Reverse Complements Problem
Assignment #: 01
Problem ID: H
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Elusive-than-Others-9/#step-5
'''

from scripts import ReverseComplementDNA as RevComp
from Assignment_01G import MismatchList

with open('data/stepic_1h.txt') as input_data:
	dna, [k, d] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]

# Use a dictionary to count the occurence of each k-mer and its reverse complement with up to d mismatches on each.
mismatch_dict = {}
for i in xrange(len(dna)-k+1):
	for kmer in MismatchList(dna[i:i+k], d)+MismatchList(RevComp(dna[i:i+k]), d):
		if kmer in mismatch_dict:
			mismatch_dict[kmer] += 1
		else:
			mismatch_dict[kmer] = 1

# Computing the maximum value is somewhat time consuming to repeat, so only do it once!
max_val = max(mismatch_dict.values())
kmers = [item[0] for item in mismatch_dict.items() if item[1] == max_val]

print ' '.join(kmers)
with open('output/Assignment_01H.txt', 'w') as output_data:
	output_data.write(' '.join(kmers))
