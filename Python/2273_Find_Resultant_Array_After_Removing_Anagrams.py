# Author: Kaustav Ghosh
# Problem: 2273. Find Resultant Array After Removing Anagrams
# URL: https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
# Difficulty: Easy
#
# Approach:
# Keep the first word. For each subsequent word, only add it to result
# if its sorted characters differ from the previous kept word's sorted characters.

class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])
        return result
