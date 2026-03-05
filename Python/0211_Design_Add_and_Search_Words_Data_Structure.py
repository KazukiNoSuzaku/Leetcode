# Design a data structure that supports adding new words and finding if a string matches
# any previously added string.
# - WordDictionary() Initializes the object.
# - void addWord(word) Adds word to the data structure, it can be matched later.
# - bool search(word) Returns true if there is any string in the data structure that matches
#   word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

# Example:
# Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
#        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output: [null,null,null,null,false,true,true,true]

# Constraints:
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.

# Author: Kaustav Ghosh

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            c = word[i]
            if c == '.':
                return any(dfs(child, i + 1) for child in node.children.values())
            if c not in node.children:
                return False
            return dfs(node.children[c], i + 1)
        return dfs(self.root, 0)
