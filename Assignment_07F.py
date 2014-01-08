#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Linear Space Alignment
Assignment #: 07
Problem ID: F
URL: https://stepic.org/Bioinformatics-Algorithms-2/SpaceEfficient-Sequence-Alignment-250/step/14
'''


def space_efficient_global_alignment(v, w, scoring_matrix, sigma):
    '''Return the global alignment of v and w using a linear space algorithm.'''
    from Assignment_06E import global_alignment
    from Assignment_07E import middle_edge

    def linear_space_alignment2(top, bottom, left, right):
        '''Constructs the global alignment path using linear space.'''

        if left == right:
            return [v[top:bottom], '-'*(bottom - top)]

        elif top == bottom:
            return ['-'*(right - left), w[left:right]]

        elif bottom - top == 1 or right - left == 1:
            return global_alignment(v[top:bottom], w[left:right], scoring_matrix, sigma)[1:]

        else:
            # Get the middle edge and the corresponding nodes.
            mid_node, next_node = middle_edge(v[top:bottom], w[left:right], scoring_matrix, sigma)

            # Shift the nodes appropriately, as they currently don't alighn with the top/left starting points.
            mid_node = tuple(map(sum, zip(mid_node, [top, left])))
            next_node = tuple(map(sum, zip(next_node, [top, left])))

            # Get the character in each alignment corresponding to the current middle edge.
            # (Take the index modulo the string length to avoid IndexErrors if we reach the end of a string but still have -'s to append.)
            current = [['-', v[mid_node[0] % len(v)]][next_node[0] - mid_node[0]], ['-', w[mid_node[1] % len(w)]][next_node[1] - mid_node[1]]]

            # Recursively divide and conquer to generate the alignment.
            A = linear_space_alignment2(top, mid_node[0], left, mid_node[1])
            B = linear_space_alignment2(next_node[0], bottom, next_node[1], right)
            return [A[i] + current[i] + B[i] for i in xrange(2)]

    # Get the alignment and alignment score.
    v_aligned, w_aligned = linear_space_alignment2(0, len(v), 0, len(w))
    score = sum([-sigma if '-' in pair else scoring_matrix[pair] for pair in zip(v_aligned, w_aligned)])

    return str(score), v_aligned, w_aligned


if __name__ == '__main__':
    from scripts import BLOSUM62

    # Read the input data.
    with open('data/stepic_7f.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]

    # Get the alignment.
    alignment = space_efficient_global_alignment(word1, word2, BLOSUM62(), 5)

    # Print and save the answer.
    print '\n'.join(alignment)
    with open('output/Assignment_07F.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))
