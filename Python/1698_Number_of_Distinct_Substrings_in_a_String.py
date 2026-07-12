# Author: Kaustav Ghosh
# Problem: Number of Distinct Substrings in a String (Premium)
# Approach: Insert every suffix into a trie; each newly created node corresponds to exactly one distinct substring, so the total new nodes is the answer

class Solution(object):
    def countDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        root = {}
        count = 0
        n = len(s)
        for i in range(n):
            node = root
            for j in range(i, n):
                ch = s[j]
                if ch not in node:
                    node[ch] = {}
                    count += 1  # a brand-new substring
                node = node[ch]
        return count
