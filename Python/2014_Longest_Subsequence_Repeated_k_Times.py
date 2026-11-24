# Author: Kaustav Ghosh
# Problem: Longest Subsequence Repeated k Times
# Approach: Since the string is shorter than eight times the repeat count, the answer can hold at most seven characters, and only letters appearing at least that many times can take part, which likewise leaves at most seven usable letters. That makes a breadth-first search over candidate strings feasible: every valid answer has a valid answer as its prefix, so each level extends only the strings that already repeat enough times, which prunes the space sharply. Testing a candidate is a single greedy sweep of the string counting how many complete copies can be matched in order, and because the letters are tried in descending order and the search deepens level by level, the last candidate accepted at the deepest level is the longest and lexicographically largest.

class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        from collections import Counter
        counts = Counter(s)
        usable = sorted([letter for letter in counts if counts[letter] >= k], reverse=True)

        def repeats(candidate):
            position = 0
            copies = 0
            width = len(candidate)
            for letter in s:
                if letter == candidate[position]:
                    position += 1
                    if position == width:
                        position = 0
                        copies += 1
                        if copies == k:
                            return True
            return False

        best = ''
        frontier = ['']
        while frontier:
            following = []
            for prefix in frontier:
                for letter in usable:
                    candidate = prefix + letter
                    if repeats(candidate):
                        following.append(candidate)
                        if len(candidate) > len(best) or (
                                len(candidate) == len(best) and candidate > best):
                            best = candidate
            frontier = following
        return best
