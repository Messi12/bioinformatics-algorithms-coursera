#!/usr/bin/env python
'''A Bioinformatics Algorithms script containing a trie data structure.'''


class Trie(object):
    """Constucts a trie for the given words."""
    def __init__(self, words):
        """Initialize the nodes and edges and add the given words."""

        # A lambda function to create nodes.
        # 'parent' = parent node number
        # 'children' = list of children node numbers.
        # 'depth' = length of substring up to the node.
        # 'end' = boolean to determine if the node corresponds to the last character of an inserted word.
        self.create_node = lambda p, d: {'parent':p, 'children':[], 'depth':d, 'end':False}

        # Initialize nodes and edges.
        self.nodes = {1:self.create_node(0,0)}
        self.edges = {}

        # Construct the trie by adding the words.
        if type(words) is str:
            self._add_word(words)
        else:
            for word in words:
                self._add_word(word)

    def _add_word(self, current_word):
        """Adds a word to the trie."""

        # Get the insertion node and portion of the word to insert.
        insertion_node, insertion_substring = self._insert_location(current_word)

        # Begin inserting at the insertion node.
        for i in xrange(len(insertion_substring)):

            # Get the new node number.
            new_node = len(self.nodes) + 1

            # Add the new node to the trie, and add parent/depth/child information.
            self.nodes[new_node] = self.create_node(insertion_node, self.nodes[insertion_node]['depth']+1)
            self.nodes[insertion_node]['children'].append(new_node)

            # Add the new edge to the trie.
            self.edges[insertion_node, new_node] = insertion_substring[i]

            # Move to the new node and continue insertion.
            insertion_node = new_node

        # Mark the last node as an end node, as it is the end of the word added.
        self.nodes[insertion_node]['end'] = True

    def _insert_location(self, word_to_add, current_node=1):
        """Traverses the trie to determine the insertion point of the given word."""

        # This happends if the word we're trying to add is already a substring of an added word.
        if word_to_add == '':
            return current_node, word_to_add

        # Search all child nodes for a match.
        for child_node in self.nodes[current_node]['children']:
            if self.edges[current_node, child_node] == word_to_add[0]:
                # Move to the child node if we have a match.
                return self._insert_location(word_to_add[1:], child_node)

        # If we reach this point, there is no character match.
        return current_node, word_to_add

    def word_up_to_node(self, node_num):
        """Returns the word associated with a traversal up to the given node."""

        node_word = ''
        while self.nodes[node_num]['parent'] != 0:
            node_word += self.edges[self.nodes[node_num]['parent'], node_num]
            node_num = self.nodes[node_num]['parent']

        # We travelled backwards, so reverse the word.
        return node_word[::-1]

    def prefix_in_trie(self, word_to_check, current_node=1):
        """Traverses the trie to determine if a prefix of the given word matches a pattern in the trie."""

        if self.nodes[current_node]['end'] is True:
            # If we hit an end node then we've found a matching pattern as a prefix.
            return True
        elif word_to_check == '':
            # If we've exhausted the word_to_check then no prefix of it matches an entire pattern in the trie.
            return False

        # Search all child nodes for a match.
        for child_node in self.nodes[current_node]['children']:
            if self.edges[current_node, child_node] == word_to_check[0]:
                # Move to the child node if we have a match.
                return self.prefix_in_trie(word_to_check[1:], child_node)

        # If we reach this point, there is no character match, and hence no prefix matching a pattern in the trie.
        return False
