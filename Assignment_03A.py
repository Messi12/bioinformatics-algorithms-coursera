#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Motif Enumeration
Assignment #: 03
Problem ID: A
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Motif-Finding-Is-More-Difficult-Than-You-Think-156/#step-7
'''

from Assignment_01G import MismatchList

with open('data/stepic_3a.txt') as input_data:
	k, d = map(int, input_data.readline().split())
	dna_list = [line.strip() for line in input_data.readlines()]

# Generate sets of (k,d)-motifs for each dna sequence in the list.
motif_sets = [{kmer for i in xrange(len(dna)-k+1) for kmer in MismatchList(dna[i:i+k], d)} for dna in dna_list]

# Intersect all sets to get the common elements.  The answers are displayed as sorted, so we'll sort too.
motifs = sorted(list(reduce(lambda a,b: a&b, motif_sets)))

# Print and save the answer.
print ' '. join(motifs)
with open('output/Assignment_03A.txt', 'w') as output_data:
	output_data.write(' '.join(motifs))
