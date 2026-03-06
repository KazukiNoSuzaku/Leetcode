# Design a data structure that will be initialized with a string array, and then it should
# answer queries of the shortest distance between two different strings from the array.
# Implement the WordDistance class:
# - WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
# - int shortest(String word1, String word2) returns the shortest distance between word1 and word2.

# Example 1:
# Input: ["WordDistance","shortest","shortest"]
#        [[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]
# Output: [null,3,1]

# Constraints:
# 1 <= wordsDict.length <= 3 * 10^4
# At most 5000 calls will be made to shortest.

# Author: Kaustav Ghosh

class WordDistance(object):
    def __init__(self, wordsDict):
        self.positions = {}
        for i, w in enumerate(wordsDict):
            self.positions.setdefault(w, []).append(i)

    def shortest(self, word1, word2):
        p1, p2 = self.positions[word1], self.positions[word2]
        i = j = 0
        res = float('inf')
        while i < len(p1) and j < len(p2):
            res = min(res, abs(p1[i] - p2[j]))
            if p1[i] < p2[j]:
                i += 1
            else:
                j += 1
        return res
