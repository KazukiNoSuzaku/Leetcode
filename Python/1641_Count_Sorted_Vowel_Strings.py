# Author: Kaustav Ghosh
# Problem: Count Sorted Vowel Strings
# Approach: A sorted string over the five vowels is determined entirely by how many of each vowel it contains, since the order is then forced, so counting strings means counting ways to split n positions among five letters. That is the classic stars-and-bars count: n indistinguishable positions separated by four dividers, giving C(n + 4, 4). Evaluating it as a product of four consecutive terms divided by twenty-four keeps the whole thing to a handful of operations with no table.

class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24
