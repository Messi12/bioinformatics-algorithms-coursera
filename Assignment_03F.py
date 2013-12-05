#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Randomized Motif Search
Assignment #: 03
Problem ID: F
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Randomized-Motif-Search-161/#step-3
'''

from random import randint
from Assignment_03D import score, profile_most_probable_kmer
from Assignment_03E import profile_with_pseudocounts

def motifs_from_profile(profile, dna, k):
	return [profile_most_probable_kmer(seq,k,profile) for seq in dna]

def randomized_motif_search(dna,k,t):
	# Randomly generate k-mers from each sequence in the dna list.
	rand_ints = [randint(0,len(dna[0])-k) for a in xrange(t)]
	motifs = [dna_list[i][r:r+k] for i,r in enumerate(rand_ints)]

	# Initialize the best score as a score higher than the highest possible score.
	best_score = [score(motifs), motifs]

	# Iterate motifs.
	while True:
		current_profile = profile_with_pseudocounts(motifs)
		motifs = motifs_from_profile(current_profile, dna_list, k)
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]
		else:
			return best_score

if __name__ == '__main__':

	with open('data/stepic_3f.txt') as input_data:
		k,t = map(int, input_data.readline().split())
		dna_list = [line.strip() for line in input_data.readlines()]

	# Initialize the best scoring motifs as a score higher than the highest possible score.
	best_motifs = [k*t, None]

	# Repeat the radomized motif search 1000 times.
	for repeat in xrange(1000):
		current_motifs = randomized_motif_search(dna_list,k,t)
		if current_motifs[0] < best_motifs[0]:
			best_motifs = current_motifs

	# Print and save the answer.
	print '\n'.join(best_motifs[1])
	with open('output/Assignment_03F.txt', 'w') as output_data:
		output_data.write('\n'.join(best_motifs[1]))
