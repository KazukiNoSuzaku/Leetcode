# Author: Kaustav Ghosh
# Problem: Maximize Number of Subsequences in a String
# Approach: Count existing subsequences equal to pattern (each second char pairs with every earlier first char). Adding one first char is best placed at the very front, gaining one per existing second char; adding one second char is best at the very end, gaining one per existing first char. Take the better of the two additions. When both pattern chars are equal, the answer is the count of pairs among count+1 copies

class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        a, b = pattern[0], pattern[1]
        if a == b:
            c = text.count(a)
            return (c + 1) * c // 2

        count = 0
        ca = 0            # number of a's seen so far
        total_a = 0
        total_b = 0
        for ch in text:
            if ch == b:
                count += ca
                total_b += 1
            if ch == a:
                ca += 1
                total_a += 1
        return count + max(total_a, total_b)
