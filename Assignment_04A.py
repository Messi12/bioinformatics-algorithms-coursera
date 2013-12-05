#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: String Composition Problem
Assignment #: 04
Problem ID: A
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/The-String-Reconstruction-Problem-197/#step-3
'''

with open('data/stepic_4a.txt') as input_data:
	k = int(input_data.readline().strip())
	text = input_data.readline().strip()

# Generate the list of all k-mers in text and sort them lexiographically.
composition = sorted([text[i:i+k] for i in xrange(len(text)-k+1)])

# Print and save the answer.
print '\n'. join(composition)
with open('output/Assignment_04A.txt', 'w') as output_data:
	output_data.write('\n'. join(composition))
