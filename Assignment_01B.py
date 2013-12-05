#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Reverse Complement Problem
Assignment #: 01
Problem ID: B
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Surprising-than-Others-3/#step-2
'''

from scripts import ReverseComplementDNA as RevComp

with open('data/stepic_1b.txt') as input_data:
	dna = input_data.read().strip()

# The script I previously wrote solves the problem...
with open('output/Assignment_01B.txt', 'w') as output_data:
	output_data.write(RevComp(dna))
