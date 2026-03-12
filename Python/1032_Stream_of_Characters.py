# Author: Kaustav Ghosh
# 1032. Stream of Characters
# https://leetcode.com/problems/stream-of-characters/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class StreamChecker(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = TrieNode()
        self.stream = []
        for word in words:
            node = self.root
            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.append(letter)
        node = self.root
        for ch in reversed(self.stream):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_end:
                return True
        return False
