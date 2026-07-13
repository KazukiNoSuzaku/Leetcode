# Author: Kaustav Ghosh
# Problem: Construct the Lexicographically Largest Valid Sequence
# Approach: Backtrack filling the leftmost empty slot, trying the largest unused number first; number i (>1) also claims slot i+i, and 1 occupies a single slot. The first complete fill is the lexicographically largest

class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        size = 2 * n - 1
        res = [0] * size
        used = [False] * (n + 1)

        def backtrack(i):
            if i == size:
                return True
            if res[i] != 0:
                return backtrack(i + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    res[i] = 1
                    used[1] = True
                    if backtrack(i + 1):
                        return True
                    res[i] = 0
                    used[1] = False
                elif i + num < size and res[i + num] == 0:
                    res[i] = res[i + num] = num
                    used[num] = True
                    if backtrack(i + 1):
                        return True
                    res[i] = res[i + num] = 0
                    used[num] = False
            return False

        backtrack(0)
        return res
