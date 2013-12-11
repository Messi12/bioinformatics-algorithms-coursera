#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: String Reconstruction Problem
Assignment #: 05
Problem ID: B
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/From-Eulers-Theorem-to-an-Algorithm-for-Finding-Eulerian-Cycles-203/#step-6
'''

# Read the input data.
with open('data/stepic_5b.txt') as input_data:
    string_dict = {line.strip().split(' -> ')[0]:line.strip().split(' -> ')[1] for line in input_data.readlines()}

# Find the head and tail strings of the reconstructed string.
head = filter(lambda x: x not in string_dict.values(), string_dict.keys())[0]
tail = filter(lambda x: x not in string_dict.keys(), string_dict.values())[0]

# Initialize the reconstruction process, starting at the head.
reconstructed_str = head[0]
current_str = head

# Iterate over all intermediary strings, appending the first character to reconstruct the string.
while current_str != tail:
    current_str = string_dict[current_str]
    reconstructed_str += current_str[0]

# Complete the reconstruction by adding the end of the tail.
reconstructed_str += tail[1:]

# Print and save the answer.
print reconstructed_str
with open('output/Assignment_05B.txt', 'w') as output_data:
    output_data.write(reconstructed_str)
