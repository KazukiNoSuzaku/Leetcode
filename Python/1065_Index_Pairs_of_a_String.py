# Author: Kaustav Ghosh
# 1065. Index Pairs of a String
# https://leetcode.com/problems/index-pairs-of-a-string/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_end = True

        result = []
        n = len(text)
        for i in range(n):
            node = root
            for j in range(i, n):
                c = text[j]
                if c not in node.children:
                    break
                node = node.children[c]
                if node.is_end:
                    result.append([i, j])
        return result
