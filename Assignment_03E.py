#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Greedy Motif Search with Pseudocounts
Assignment #: 03
Problem ID: E
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Motif-Finding-Meets-Oliver-Cromwell-160/#step-9
'''

from Assignment_03D import score, profile_most_probable_kmer

def profile_with_pseudocounts(motifs):
	'''Returns the profile of the dna list motifs.'''
	prof = []
	for i in xrange(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		prof.append([float(col.count(nuc)+1)/float(len(col)+4) for nuc in 'ACGT'])
	return prof

if __name__ == '__main__':

	with open('data/stepic_3e.txt') as input_data:
		k,t = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]

	# Initialize the best score as a score higher than the highest possible score.
	best_score = [t*k, None]

	# Run the greedy motif search.
	for i in xrange(len(dna_list[0])-k+1):
		# Initialize the motifs as each k-mer from the first dna sequence.
		motifs = [dna_list[0][i:i+k]]
		current_profile = profile_with_pseudocounts(motifs)

		# Find the most probable k-mer in the next string, using pseudocounts.
		for j in xrange(1,t):
			motifs.append(profile_most_probable_kmer(dna_list[j],k,current_profile))
			current_profile = profile_with_pseudocounts(motifs)

		# Check to see if we have a new best scoring list of motifs.
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]

	# Print and save the answer.
	print '\n'.join(best_score[1])
	with open('output/Assignment_03E.txt', 'w') as output_data:
		output_data.write('\n'.join(best_score[1]))
