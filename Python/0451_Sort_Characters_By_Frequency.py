# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        return ''.join(ch * count for ch, count in Counter(s).most_common())
