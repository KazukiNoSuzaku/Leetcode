# Author: Kaustav Ghosh
# Problem: Check Distances Between Same Letters
# Approach: Remember where each letter first appears; at its second appearance the number of letters in between is the index gap minus one, which must equal that letter's entry in distance

class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        first = {}
        for i, ch in enumerate(s):
            if ch in first:
                if i - first[ch] - 1 != distance[ord(ch) - ord('a')]:
                    return False
            else:
                first[ch] = i
        return True
