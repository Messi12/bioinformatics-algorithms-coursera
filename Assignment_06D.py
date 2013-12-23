#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Longest Path in a DAG Problem
Assignment #: 06
Problem ID: D
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Backtracking-in-the-Alignment-Graph-245/#step-7
'''


def topological_ordering(graph):
    '''Returns a topological ordering for the given graph.'''
    # Initialize and covert variables appropriately.
    graph = set(graph)
    ordering = []
    candidates = list({edge[0] for edge in graph} - {edge[1] for edge in graph})

    # Get the topological ordering.
    while len(candidates) != 0:
        # Add the next candidate to the ordering.
        ordering.append(candidates[0])

        # Remove outgoing edges and store outgoing nodes.
        temp_nodes = []
        for edge in filter(lambda e: e[0] == candidates[0], graph):
            graph.remove(edge)
            temp_nodes.append(edge[1])

        # Add outgoing nodes to candidates list if it has no other incoming edges.
        for node in temp_nodes:
            if node not in {edge[1] for edge in graph}:
                candidates.append(node)

        # Remove the current candidate.
        candidates = candidates[1:]

    return ordering


def longest_path(graph, edges, source, sink):
    '''Returns the length and path of the longest path.'''
    # Get the topological ordering from the source to sink, not including the source.
    top_order = topological_ordering(graph.keys())
    top_order = top_order[top_order.index(source)+1:top_order.index(sink)+1]

    # Initialize S and backtrack.
    S = {node:-100 for node in {edge[0] for edge in graph.keys()} | {edge[1] for edge in graph.keys()}}
    S[source] = 0
    backtrack = {node:None for node in top_order}

    # Iterate through the topological order to get the distances, store predecessors in backtrack.
    for node in top_order:
        try:
            S[node], backtrack[node] = max(map(lambda e: [S[e[0]] + graph[e], e[0]], filter(lambda e: e[1] == node, graph.keys())), key=lambda p:p[0])
        # ValueError occurs if max() is empty, i.e. the given node has no predecessor.  This is fine, as top_order can include unrealted vertices.
        # Ignore such nodes, as they will not factor into the longest path from source to sink.
        except ValueError:
            pass

    # Backtrack to get the longest path.
    path = [sink]
    while path[0] != source:
        path = [backtrack[path[0]]] + path

    return S[sink], path

if __name__ == '__main__':

    # Read the input data.
    with open('data/stepic_6d.txt') as input_data:
        source, sink = [int(input_data.readline()) for repeat in xrange(2)]

        # Construct the edges and edge weights.
        edges, edge_weight = {}, {}
        for pair in [line.strip().split('->') for line in input_data.readlines()]:
            if int(pair[0]) not in edges:
                edges[int(pair[0])] = [int(pair[1].split(':')[0])]
            else:
                edges[int(pair[0])].append(int(pair[1].split(':')[0]))

            edge_weight[int(pair[0]), int(pair[1].split(':')[0])] = int(pair[1].split(':')[1])

    # Get the length and path of the longest path.
    length, path = longest_path(edge_weight, edges, source, sink)

    # Convert to strings and format properly.
    lenth = str(length)
    path = '->'.join(map(str, path))

    # Print and save the answer.
    print '\n'.join([lenth,path])
    with open('output/Assignment_06D.txt', 'w') as output_data:
        output_data.write('\n'.join([lenth,path]))
