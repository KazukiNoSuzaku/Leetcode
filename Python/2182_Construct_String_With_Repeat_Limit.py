# Author: Kaustav Ghosh
# 2182. Construct String With Repeat Limit
# https://leetcode.com/problems/construct-string-with-repeat-limit/
# Difficulty: Medium
#
# Approach: Greedy with frequency array. Always use the largest available
# character up to `repeatLimit` times. If more remain, insert the next
# largest character once to break the streak, then continue.
# Time: O(n + 26), Space: O(26)

class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        result = []
        i = 25  # pointer to largest available char

        while i >= 0:
            if freq[i] == 0:
                i -= 1
                continue
            # use up to repeatLimit of char i
            use = min(freq[i], repeatLimit)
            result.append(chr(ord('a') + i) * use)
            freq[i] -= use

            if freq[i] > 0:
                # find next largest char to insert as separator
                j = i - 1
                while j >= 0 and freq[j] == 0:
                    j -= 1
                if j < 0:
                    break
                result.append(chr(ord('a') + j))
                freq[j] -= 1

        return ''.join(result)
