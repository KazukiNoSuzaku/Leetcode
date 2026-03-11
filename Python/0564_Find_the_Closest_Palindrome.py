# Given a string n representing an integer, return the closest integer (not including itself)
# which is a palindrome. If there is a tie, return the smaller one.

# Author: Kaustav Ghosh

class Solution(object):
    def nearestPalindromic(self, n):
        num = int(n)
        length = len(n)
        candidates = set()
        # Edge: all 9s of length-1 and 10^length + 1
        candidates.add(10**(length-1) - 1)
        candidates.add(10**length + 1)
        # Mirror first half
        prefix = int(n[:(length+1)//2])
        for delta in [-1, 0, 1]:
            p = str(prefix + delta)
            if length % 2 == 0:
                mirror = p + p[::-1]
            else:
                mirror = p + p[-2::-1]
            candidates.add(int(mirror))
        candidates.discard(num)
        return str(min(candidates, key=lambda x: (abs(x - num), x)))
