#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Pattern Matching Problem
Assignment #: 01
Problem ID: C 
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Surprising-than-Others-3/#step-5
'''

with open('data/stepic_1c.txt') as input_data:
	pattern, text = [line.strip() for line in input_data.readlines()]

pattern_loc = []
for i in xrange(len(text)-len(pattern)+1):
	if text[i:i+len(pattern)] == pattern:
		pattern_loc.append(str(i))

print ' '.join(pattern_loc)
with open('output/Assignment_01C.txt', 'w') as output_data:
	output_data.write(' '.join(pattern_loc))
