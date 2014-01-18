#!/usr/bin/env python
'''A Bioinformatics Algorithms script containing a generalized suffix tree class.'''


class Node(object):
    """Node class to be used in the GeneralizedSuffixTree class."""
    def __init__(self, parent_num, words=set()):
        """Initialize parameters."""
        self.parent = parent_num
        self.children = []
        self.words = words

    def update_parent(self, new_parent_num):
        """Update the nodes parent."""
        self.parent = new_parent_num

    def add_child(self, node_num):
        """Add a child node to the node."""
        self.children.append(node_num)

    def remove_child(self, node_num):
        """Remove a child from the node."""
        self.children.remove(node_num)

    def add_word(self, word_num):
        """Stores the indices of words in the word_list that traverse through the node."""
        self.words.add(word_num)


class Edge(object):
    """Edge class to be used in the GeneralizedSuffixTree class."""
    def __init__(self, word, start_index, stop_index):
        """Initialize parameters."""
        self.word = word
        self.start_index = start_index
        self.stop_index = stop_index


class GeneralizedSuffixTree(object):
    """Constucts a generalized suffix tree for the given words."""
    def __init__(self, words):
        """Initialize parameters and build the tree with the given words."""

        # Initialize parameters.
        self.word_list = []
        self.nodes = [Node(-1)]
        self.edges = {}

        # Add the words to the generalized suffix tree.
        if type(words) is list:
            for word in words:
                self._add_word(word)
        elif type(words) is str:
            self._add_word(words)

    def _add_word(self, current_word):
        """Adds a word to the generalized suffix tree."""

        # Add the properly indexed out of alphabet character to the current word, and add it to the word list and root node.
        # These need to be distinct (i.e. $0, $1, ..., $N), to distinguish between multiple words in the tree.
        current_word = current_word + ['', '$'][current_word[-1] != '$'] + str(len(self.word_list))
        self.word_list.append(current_word)
        self.nodes[0].add_word(len(self.word_list)-1)

        # Add each suffix to the generalized suffix tree.
        for i in xrange(current_word.index('$')+1):
            # Get the insertion point and associated suffix.
            insertion_parent, insertion_suffix = self._insert_node(current_word[i:])

            # Create the new node, and add it as a child to its parent node.
            self.nodes.append(Node(insertion_parent, {len(self.word_list)-1}))
            self.nodes[insertion_parent].add_child(len(self.nodes)-1)

            # Create the edge associated to with the new node.
            self.edges[insertion_parent, len(self.nodes)-1] = Edge(len(self.word_list)-1, len(current_word)-len(insertion_suffix), len(current_word))

    def _insert_node(self, suffix, current_node=0):
        """Traverses the tree to determine the insertion point of the given suffix."""

        # Done if we've reached the out of alphabet character.
        if suffix[0] == '$':
            return current_node, suffix

        # Check all childen nodes to determine if we can traverse further down the tree.
        for child_num in self.nodes[current_node].children:
            e = self.edges[current_node, child_num]
            edge_word = self.word_list[e.word][e.start_index:e.stop_index]

            # If the entire edge appears as a prefix of the suffix, move to the child node  and traverse further down the tree.
            if suffix[:len(edge_word)] == edge_word:
                self.nodes[child_num].add_word(len(self.word_list)-1)
                return self._insert_node(suffix[len(edge_word):], child_num)

            # If the edge partially overlaps in prefix of the current suffix, split the edge and insert at the split.
            elif suffix[0] == edge_word[0]:
                # Determine how many charaters overlap.
                i = 0
                while suffix[i] == edge_word[i] != '$':
                    i += 1

                # Split the edge at the end of the overlap.
                return self._split_edge(current_node, child_num, i), suffix[i:]

        return current_node, suffix

    def _split_edge(self, parent_num, child_num, split_pos):
        """
        Splits the edge between the given parent and child nodes at the given split position.
        Inserts a new node at the split position and returns the index of the new node.
        """

        # Create the new node.
        new_node = len(self.nodes)
        self.nodes.append(Node(parent_num, words={len(self.word_list)-1, self.edges[parent_num, child_num].word}))
        self.nodes[new_node].add_child(child_num)

        # Add new_node as a child of parent_num.  Remove child_num from children list.
        self.nodes[parent_num].add_child(new_node)
        self.nodes[parent_num].remove_child(child_num)

        # Update child_num's parent to new_node.
        self.nodes[child_num].update_parent(new_node)

        # Create the new edges.
        old_edge = self.edges[parent_num, child_num]
        self.edges[parent_num, new_node] = Edge(old_edge.word, old_edge.start_index, old_edge.start_index + split_pos)
        self.edges[new_node, child_num] = Edge(old_edge.word, old_edge.start_index + split_pos, old_edge.stop_index)

        # Remove the old edge.
        del self.edges[parent_num, child_num]

        return new_node

    def edge_word(self, e):
        """Returns the substring associated with a given edge."""
        return self.word_list[e.word][e.start_index:e.stop_index]

    def word_up_to_node(self, node_num):
        """Returns the substring associated with a traversal to the given node."""
        node_word = ''
        while self.nodes[node_num].parent != -1:
            # Prepend the substring associated with each edge until we hit the root of the generalized suffix tree.
            node_word = self.edge_word(self.edges[self.nodes[node_num].parent, node_num]) + node_word
            node_num = self.nodes[node_num].parent

        return node_word

    def node_depth(self, node_num):
        """Returns the length of the substring traversal up to the given node, discounting the out of alphabet character."""
        node_word = self.word_up_to_node(node_num)
        return len(node_word) - [0, 2]['$' in node_word]
