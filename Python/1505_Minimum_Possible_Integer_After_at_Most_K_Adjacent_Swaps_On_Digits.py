# Author: Kaustav Ghosh
# Problem: Minimum Possible Integer After at Most K Adjacent Swaps On Digits
# Approach: Greedily pick smallest reachable digit within remaining swap budget, bubble it forward

class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num = list(num)
        n = len(num)
        i = 0
        while k > 0 and i < n:
            min_pos = i
            for j in range(i + 1, min(i + k + 1, n)):
                if num[j] < num[min_pos]:
                    min_pos = j
            while min_pos > i:
                num[min_pos], num[min_pos - 1] = num[min_pos - 1], num[min_pos]
                min_pos -= 1
                k -= 1
            i += 1
        return ''.join(num)
