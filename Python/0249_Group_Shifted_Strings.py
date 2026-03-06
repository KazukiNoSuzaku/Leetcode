# We can shift a string by shifting each of its letters to its successive letter.
# Given a list of strings, group all strings that belong to the same shifting sequence.

# Example 1:
# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

# Constraints:
# 1 <= strings.length <= 200
# 1 <= strings[i].length <= 50
# strings[i] consists of lowercase English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def groupStrings(self, strings):
        groups = {}
        for s in strings:
            key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
            groups.setdefault(key, []).append(s)
        return list(groups.values())
