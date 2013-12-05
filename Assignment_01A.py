#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic.

Problem Title: Creating a Distance Matrix
Assignment #: 01
Problem ID: A 
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Hidden-Messages-in-the-Replication-Origin-2/#step-4
'''

with open('data/stepic_1a.txt') as input_data:
	dna, k = [line.strip() for line in input_data.readlines()]
	k = int(k)

kmer_dict = dict()

for i in xrange(len(dna)-k+1):
	if dna[i:i+k] in kmer_dict:
		kmer_dict[dna[i:i+k]] += 1
	else:
		kmer_dict[dna[i:i+k]] = 1

kmers = [item[0] for item in kmer_dict.items() if item[1] == max(kmer_dict.values())]

print ' '.join(kmers)
with open('output/Assignment_01A.txt', 'w') as output_data:
	output_data.write(' '.join(kmers))
