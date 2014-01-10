#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Shared k-mers Problem
Assignment #: 08
Problem ID: D
URL: https://stepic.org/Bioinformatics-Algorithms-2/Synteny-Block-Construction-289/step/2
'''


def shared_kmers(dna1, dna2, k):
    '''Returns a list of positions for shared kmers (up to reverse complement) in dna1 and dna2.'''
    from scripts import ReverseComplementDNA as rev_comp

    # Initialize the dictionary to store kmers.
    dna_dict = {}

    # Store the starting index of all kmers contained in dna1 in a list keyed to the kmer.
    for i in xrange(len(dna1) - k + 1):
        # Add the ith kmer.
        if dna1[i:i+k] in dna_dict:
            dna_dict[dna1[i:i+k]].append(i)
        else:
            dna_dict[dna1[i:i+k]] = [i]

        # Add the reverse complement of the ith kmer.
        if rev_comp(dna1[i:i+k]) in dna_dict:
            dna_dict[rev_comp(dna1[i:i+k])].append(i)
        else:
            dna_dict[rev_comp(dna1[i:i+k])] = [i]

    # Use a set to remove possible duplicate entries.
    common_kmers = set()

    # Check kmers in dna2 against those in dna1, adding matching indices to common_kmers.
    for j in xrange(len(dna2) - k + 1):
        # Check the jth kmer.
        if dna2[j:j+k] in dna_dict:
            for x in dna_dict[dna2[j:j+k]]:
                common_kmers.add((x,j))

        # Check the reverse complement of the jth kmer.
        if rev_comp(dna2[j:j+k]) in dna_dict:
            for x in dna_dict[rev_comp(dna2[j:j+k])]:
                common_kmers.add((x,j))

    return common_kmers

if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_8d.txt') as input_data:
        k = int(input_data.readline().strip())
        dna1, dna2 = [line.strip() for line in input_data.readlines()]

    # Get the shared kmers.  Sorting doesn't add significant time and makes the result more readable.
    common = map(str, sorted(shared_kmers(dna1, dna2, k)))

    # Print and save the answer.
    print '\n'.join(common)
    with open('output/Assignment_08D.txt', 'w') as output_data:
        output_data.write('\n'.join(common))
