# Given a string array words, return the maximum value of length(word[i]) * length(word[j])
# where the two words do not share common letters. If no such two words exist, return 0.

# Example 1:
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

# Example 2:
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4

# Constraints:
# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists only of lowercase English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def maxProduct(self, words):
        masks = [0] * len(words)
        for i, w in enumerate(words):
            for c in w:
                masks[i] |= 1 << (ord(c) - ord('a'))
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res
