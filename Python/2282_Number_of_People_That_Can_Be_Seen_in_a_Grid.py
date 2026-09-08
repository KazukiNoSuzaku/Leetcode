# Author: Kaustav Ghosh
# Problem: Number of People That Can Be Seen in a Grid
# Approach: Visibility to the right and downward is a 1D "people in a queue can see each other" problem applied independently to every row and every column. Sweep each line from the far end with a strictly-decreasing monotonic stack: pop everyone shorter (each is visible), see one taller-or-equal person if present, and merge equal heights so a same-height neighbor blocks anyone beyond. Sum the row and column visibility counts

class Solution(object):
    def seePeople(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(heights), len(heights[0])
        answer = [[0] * n for _ in range(m)]

        def sweep(get, length, add):
            # get(k) -> height at position k; add(k, cnt) records the count
            stack = []
            for i in range(length - 1, -1, -1):
                h = get(i)
                cnt = 0
                while stack and stack[-1] < h:
                    stack.pop()
                    cnt += 1
                if stack:
                    cnt += 1
                if stack and stack[-1] == h:
                    stack.pop()  # merge equal heights (keep stack strictly decreasing)
                stack.append(h)
                add(i, cnt)

        # rows (visibility to the right)
        for r in range(m):
            sweep(lambda c, r=r: heights[r][c], n,
                  lambda c, cnt, r=r: answer[r].__setitem__(c, answer[r][c] + cnt))
        # columns (visibility downward)
        for c in range(n):
            sweep(lambda r, c=c: heights[r][c], m,
                  lambda r, cnt, c=c: answer[r].__setitem__(c, answer[r][c] + cnt))
        return answer
