#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Spectral Convolution Problem
Assignment #: 02
Problem ID: F
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/The-Spectral-Convolution-Saves-the-Day-104/#step-4
'''

with open('data/stepic_2f.txt') as input_data:
	spec = map(int, input_data.read().strip().split())

# The spectrum isn't sorted, so find all differences and filter out the non-positive.
convolution = [str(i-j) for i in spec for j in spec if i-j > 0]

# Print and save the answer.
print ' '.join(convolution)
with open('output/Assignment_02F.txt', 'w') as output_data:
	output_data.write(' '.join(convolution))
