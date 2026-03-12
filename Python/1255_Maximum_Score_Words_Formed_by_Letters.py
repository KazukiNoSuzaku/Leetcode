# Author: Kaustav Ghosh
# Bitmask DP over all subsets of words, check letter availability

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        from collections import Counter
        letter_count = Counter(letters)
        n = len(words)
        result = 0

        for mask in range(1 << n):
            needed = Counter()
            word_score = 0
            for i in range(n):
                if mask & (1 << i):
                    for c in words[i]:
                        needed[c] += 1
                        word_score += score[ord(c) - ord('a')]
            if all(needed[c] <= letter_count[c] for c in needed):
                result = max(result, word_score)
        return result
