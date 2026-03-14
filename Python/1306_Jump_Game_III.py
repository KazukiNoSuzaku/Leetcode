# Starting at index start, you can jump to i+arr[i] or i-arr[i].
# Return true if you can reach any index with value 0.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        n = len(arr)
        q = deque([start])
        visited = set([start])
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            for ni in [i + arr[i], i - arr[i]]:
                if 0 <= ni < n and ni not in visited:
                    visited.add(ni)
                    q.append(ni)
        return False
