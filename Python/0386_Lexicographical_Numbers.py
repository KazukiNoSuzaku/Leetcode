# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
# You must write an algorithm that runs in O(n) time and uses O(1) extra space.

# Author: Kaustav Ghosh

class Solution(object):
    def lexicalOrder(self, n):
        res = []
        cur = 1
        while len(res) < n:
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur + 1 > n:
                    cur //= 10
                cur += 1
        return res
