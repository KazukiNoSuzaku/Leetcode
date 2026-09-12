# Author: Kaustav Ghosh
# Problem: Spiral Matrix IV
# Approach: Fill an m x n grid (initialized to -1) by walking it in clockwise spiral order, placing successive linked-list values until the list runs out; untouched cells keep -1

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        grid = [[-1] * n for _ in range(m)]
        top, bottom, left, right = 0, m - 1, 0, n - 1
        node = head
        while node and top <= bottom and left <= right:
            for c in range(left, right + 1):
                if not node:
                    break
                grid[top][c] = node.val
                node = node.next
            top += 1
            for r in range(top, bottom + 1):
                if not node:
                    break
                grid[r][right] = node.val
                node = node.next
            right -= 1
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    if not node:
                        break
                    grid[bottom][c] = node.val
                    node = node.next
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    if not node:
                        break
                    grid[r][left] = node.val
                    node = node.next
                left += 1
        return grid
