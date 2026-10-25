# Author: Kaustav Ghosh
# Problem: Determine if String Halves Are Alike
# Approach: The length is guaranteed even, so the split point is fixed and the only quantity needed is how many vowels each half holds; counting them against a set of both cases avoids any case folding, and the two counts are compared directly without building the halves as separate strings.

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set('aeiouAEIOU')
        half = len(s) // 2
        front = sum(1 for i in range(half) if s[i] in vowels)
        back = sum(1 for i in range(half, len(s)) if s[i] in vowels)
        return front == back
