# Author: Kaustav Ghosh
# Problem: Kth Smallest Instructions
# Approach: Since 'H' sorts before 'V', every instruction beginning with 'H' precedes every instruction beginning with 'V', so the k-th string can be built one character at a time without generating any others: at each step the number of completions that start with 'H' is the number of ways to arrange the remaining moves after committing that 'H', which is a single binomial coefficient. If k falls within that block the character is 'H'; otherwise k is reduced by the block's size and the character is 'V'. Once the down moves are exhausted the rest is forced, and the binomials stay small because the total number of moves is at most thirty.

class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        def choose(n, r):
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            result = 1
            for i in range(r):
                result = result * (n - i) // (i + 1)
            return result

        down, right = destination
        instructions = []
        while right > 0 and down > 0:
            starting_with_h = choose(right - 1 + down, down)
            if k <= starting_with_h:
                instructions.append('H')
                right -= 1
            else:
                k -= starting_with_h
                instructions.append('V')
                down -= 1
        instructions.append('H' * right)
        instructions.append('V' * down)
        return ''.join(instructions)
