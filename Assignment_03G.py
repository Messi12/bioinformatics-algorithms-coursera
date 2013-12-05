#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic.

Problem Title: Gibbs Sampler
Assignment #: 03
Problem ID: G
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Gibbs-Sampling-163/#step-4
'''

from random import randint
from Assignment_03D import score, profile_most_probable_kmer
from Assignment_03E import profile_with_pseudocounts

def gibbs_sampler(dna,k,t,N):
	# Randomly generate k-mers from each sequence in the dna list.
	rand_ints = [randint(0,len(dna[0])-k) for a in xrange(t)]
	motifs = [dna_list[i][r:r+k] for i,r in enumerate(rand_ints)]

	# Initialize the best score as a score higher than the highest possible score.
	best_score = [score(motifs), motifs]

	# Iterate motifs.
	for i in xrange(N):
		r = randint(0,t-1)
		current_profile = profile_with_pseudocounts([motif for index, motif in enumerate(motifs) if index!=r])
		# print 'a: ', motifs
		motifs = [profile_most_probable_kmer(dna[index],k,current_profile) if index == r else motif for index,motif in enumerate(motifs)]
		# print 'b: ', motifs
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]

	return best_score

if __name__ == '__main__':

	with open('data/stepic_3g.txt') as input_data:
		k,t,N = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]

	# Initialize the best scoring motifs as a score higher than the highest possible score.
	best_motifs = [k*t, None]

	# Repeat the radomized motif search 20 times.
	for repeat in xrange(20):
		current_motifs = gibbs_sampler(dna_list,k,t,N)
		if current_motifs[0] < best_motifs[0]:
			best_motifs = current_motifs

	# Print and save the answer.
	print '\n'.join(best_motifs[1])
	with open('output/Assignment_03G.txt', 'w') as output_data:
		output_data.write('\n'.join(best_motifs[1]))
