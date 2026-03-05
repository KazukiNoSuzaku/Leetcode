# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
# store and retrieve keys in a dataset of strings.
# Implement the Trie class:
# - Trie() Initializes the trie object.
# - void insert(String word) Inserts the string word into the trie.
# - boolean search(String word) Returns true if the string word is in the trie.
# - boolean startsWith(String prefix) Returns true if there is a previously inserted string
#   that has the prefix prefix, and false otherwise.

# Example:
# Input: ["Trie","insert","search","search","startsWith","insert","search"]
#        [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
# Output: [null,null,true,false,true,null,true]

# Constraints:
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.

# Author: Kaustav Ghosh

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
