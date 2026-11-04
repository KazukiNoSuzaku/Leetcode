# Author: Kaustav Ghosh
# Problem: Implement Trie II (Prefix Tree)
# Approach: Both queries are counts, so every node carries two tallies: how many stored words end exactly there and how many pass through it. Inserting walks the word and bumps the pass-through tally at each step plus the ending tally at the last node, which makes a prefix query a single descent that reads one number. Erasing is the same walk with the tallies decremented, so nodes are left in place rather than pruned; that keeps every operation proportional to the word length and, since the problem promises erase is only called on a word that is present, no tally can go negative.

class Trie(object):

    def __init__(self):
        self.children = {}
        self.through = 0
        self.ending = 0

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
            node.through += 1
        node.ending += 1

    def _walk(self, prefix):
        node = self
        for letter in prefix:
            if letter not in node.children:
                return None
            node = node.children[letter]
        return node

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        node = self._walk(word)
        return node.ending if node else 0

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self._walk(prefix)
        return node.through if node else 0

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for letter in word:
            node = node.children[letter]
            node.through -= 1
        node.ending -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
