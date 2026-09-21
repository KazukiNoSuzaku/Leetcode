# Author: Kaustav Ghosh
# Problem: Sum of Prefix Scores of Strings
# Approach: Insert every word into a trie where each node counts how many words pass through it, which is exactly the score of the prefix ending at that node. Walking a word down the trie again and adding the counts along the way gives its total score

class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        root = [0, {}]
        for word in words:
            node = root
            for ch in word:
                if ch not in node[1]:
                    node[1][ch] = [0, {}]
                node = node[1][ch]
                node[0] += 1
        scores = []
        for word in words:
            node = root
            score = 0
            for ch in word:
                node = node[1][ch]
                score += node[0]
            scores.append(score)
        return scores
