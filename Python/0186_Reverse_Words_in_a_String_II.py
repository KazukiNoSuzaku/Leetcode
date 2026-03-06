# Given a character array s, reverse the order of the words.
# Your code must solve it in-place, i.e., without allocating extra space.

# Example 1:
# Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

# Example 2:
# Input: s = ["a"]
# Output: ["a"]

# Constraints:
# 1 <= s.length <= 10^5
# s[i] is an English letter or space.
# There is at least one word in s.
# s does not contain leading or trailing spaces.
# All words are separated by a single space.

# Author: Kaustav Ghosh

class Solution(object):
    def reverseWords(self, s):
        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        reverse(0, len(s) - 1)
        start = 0
        for end in range(len(s) + 1):
            if end == len(s) or s[end] == ' ':
                reverse(start, end - 1)
                start = end + 1
