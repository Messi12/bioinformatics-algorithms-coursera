#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Greedy Motif Search
Assignment #: 03
Problem ID: D
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Greedy-Motif-Search-159/#step-5
'''

from scripts import HammingDistance

def score(motifs):
	'''Returns the score of the dna list motifs.'''
	score = 0
	for i in xrange(len(motifs[0])):
		motif = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		score += min([HammingDistance(motif, homogeneous*len(motif)) for homogeneous in 'ACGT'])
	return score

def profile(motifs):
	'''Returns the profile of the dna list motifs.'''
	prof = []
	for i in xrange(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in xrange(len(motifs))])
		prof.append([float(col.count(nuc))/float(len(col)) for nuc in 'ACGT'])
	return prof

def profile_most_probable_kmer(dna, k, prof):
	'''Return the profile most probable k-mer in a given dna sequence.'''
	# A dictionary relating nucleotides to their position within the profile.
	nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}
	# Initialize the maximum probabily.
	max_prob = [-1, None]
	# Compute the probability of the each k-mer, store it if it's currently a maximum.
	for i in xrange(len(dna)-k+1):
		current_prob = 1
		for j, nucleotide in enumerate(dna[i:i+k]):
			current_prob *= prof[j][nuc_loc[nucleotide]]
		if current_prob > max_prob[0]:
			max_prob = [current_prob, dna[i:i+k]]

	return max_prob[1]

if __name__ == '__main__':

	with open('data/stepic_3d.txt') as input_data:
		k,t = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]

	# Initialize the best score as a score higher than the highest possible score.
	best_score = [t*k, None]

	# Run the greedy motif search.
	for i in xrange(len(dna_list[0])-k+1):
		# Initialize the motifs as each k-mer from the first dna sequence.
		motifs = [dna_list[0][i:i+k]]
		current_profile = profile(motifs)

		# Find the most probable k-mer in the next string.
		for j in xrange(1,t):
			motifs.append(profile_most_probable_kmer(dna_list[j],k,current_profile))
			current_profile = profile(motifs)

		# Check to see if we have a new best scoring list of motifs.
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]

	# Print and save the answer.
	print '\n'.join(best_score[1])
	with open('output/Assignment_03D.txt', 'w') as output_data:
		output_data.write('\n'.join(best_score[1]))
