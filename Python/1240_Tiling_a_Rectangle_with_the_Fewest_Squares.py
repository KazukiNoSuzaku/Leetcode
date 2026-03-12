# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Backtracking with skyline to fill rectangle with minimum squares

class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        self.result = n * m  # worst case: all 1x1

        def backtrack(heights, count):
            if count >= self.result:
                return
            # Find the lowest point
            min_h = min(heights)
            if min_h == n:
                self.result = min(self.result, count)
                return
            # Find the leftmost lowest column
            idx = heights.index(min_h)
            # Find max width of square starting at idx
            max_side = 1
            while idx + max_side <= m and all(heights[idx + j] == min_h for j in range(max_side)) and min_h + max_side <= n:
                max_side += 1
            max_side -= 1

            for side in range(max_side, 0, -1):
                new_heights = list(heights)
                for j in range(side):
                    new_heights[idx + j] += side
                backtrack(new_heights, count + 1)

        backtrack([0] * m, 0)
        return self.result
