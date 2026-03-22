# Author: Kaustav Ghosh
# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        length = 2 * n - 1
        result = [0] * length
        used = [False] * (n + 1)

        def backtrack(idx):
            if idx == length:
                return True
            if result[idx] != 0:
                return backtrack(idx + 1)
            # Try largest number first for lexicographic order
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if num == 1:
                    result[idx] = 1
                    used[1] = True
                    if backtrack(idx + 1):
                        return True
                    result[idx] = 0
                    used[1] = False
                else:
                    j = idx + num
                    if j < length and result[j] == 0:
                        result[idx] = num
                        result[j] = num
                        used[num] = True
                        if backtrack(idx + 1):
                            return True
                        result[idx] = 0
                        result[j] = 0
                        used[num] = False
            return False

        backtrack(0)
        return result
