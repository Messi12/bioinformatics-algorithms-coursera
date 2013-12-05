#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Protein Translation Problem
Assignment #: 02
Problem ID: A
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/How-Do-Bacteria-Make-Antibiotics-96/#step-3
'''

# This is a repeat of Rosalind Problem 008: Translating RNA into Protein.
from scripts import ProteinDictRNA

with open('data/stepic_2a.txt') as input_data:
	s = input_data.read().strip()

# Dictionary translating RNA to Protein
rna_dict = ProteinDictRNA()

s_protein = ''
for i in range(0,len(s),3):
    if rna_dict[s[i:i+3]] != 'Stop':
        s_protein += rna_dict[s[i:i+3]]

print s_protein

with open('output/Assignment_02A.txt', 'w') as output_data:
	output_data.write(s_protein)
