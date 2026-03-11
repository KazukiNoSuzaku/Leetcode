# From index i, odd jumps go to the smallest j > i where nums[j] >= nums[i],
# even jumps to largest j > i where nums[j] <= nums[i].
# Return number of starting indices from which you can reach the end.

# Author: Kaustav Ghosh

class Solution(object):
    def oddEvenJumps(self, arr):
        n = len(arr)
        odd_next = [None] * n
        even_next = [None] * n
        # Build next for odd jumps: sorted by value asc, then index asc
        stack = []
        for i, _ in sorted(enumerate(arr), key=lambda x: (x[1], x[0])):
            while stack and stack[-1] < i:
                odd_next[stack.pop()] = i
            stack.append(i)
        # Build next for even jumps: sorted by value desc, then index asc
        stack = []
        for i, _ in sorted(enumerate(arr), key=lambda x: (-x[1], x[0])):
            while stack and stack[-1] < i:
                even_next[stack.pop()] = i
            stack.append(i)
        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True
        for i in range(n - 2, -1, -1):
            if odd_next[i] is not None:
                odd[i] = even[odd_next[i]]
            if even_next[i] is not None:
                even[i] = odd[even_next[i]]
        return sum(odd)
