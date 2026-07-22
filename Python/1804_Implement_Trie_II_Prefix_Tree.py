# Author: Kaustav Ghosh
# Problem: Implement Trie II (Prefix Tree) (Premium)
# Approach: Each node tracks children plus how many words end here and how many pass through, so word/prefix counts are O(length) reads and erase decrements the same counters

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.words_ending = 0
        self.words_through = 0


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
            node.words_through += 1
        node.words_ending += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        node = self._walk(word)
        return node.words_ending if node else 0

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self._walk(prefix)
        return node.words_through if node else 0

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.words_through -= 1
        node.words_ending -= 1

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
