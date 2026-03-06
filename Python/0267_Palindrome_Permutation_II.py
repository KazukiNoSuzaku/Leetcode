# Given a string s, return all the palindromic permutations (without duplicates) of it.
# You may return the answer in any order. If no palindromic permutation exists, return an empty list.

# Example 1:
# Input: s = "aabb"
# Output: ["abba","baab"]

# Example 2:
# Input: s = "abc"
# Output: []

# Constraints:
# 1 <= s.length <= 16
# s consists of only lowercase English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def generatePalindromes(self, s):
        from collections import Counter
        count = Counter(s)
        odds = [c for c, v in count.items() if v % 2 == 1]
        if len(odds) > 1:
            return []
        mid = odds[0] if odds else ''
        half = ''.join(c * (count[c] // 2) for c in count)
        res = []
        half = list(half)
        def permute(path, used):
            if len(path) == len(half):
                p = ''.join(path)
                res.append(p + mid + p[::-1])
                return
            for i in range(len(half)):
                if used[i]:
                    continue
                if i > 0 and half[i] == half[i-1] and not used[i-1]:
                    continue
                used[i] = True
                permute(path + [half[i]], used)
                used[i] = False
        half.sort()
        permute([], [False] * len(half))
        return res
