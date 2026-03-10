# Given a string s and an integer k, rearrange s such that the same characters
# are at least k distance apart. If it is not possible to rearrange the string,
# return an empty string "".

# Example 1:
# Input: s = "aabbcc", k = 3
# Output: "abcabc"

# Example 2:
# Input: s = "aaabc", k = 3
# Output: ""

# Constraints:
# 1 <= s.length <= 3 * 10^5
# s consists of only lowercase English letters.
# 0 <= k <= s.length

# Author: Kaustav Ghosh

import heapq
from collections import Counter, deque

class Solution(object):
    def rearrangeString(self, s, k):
        if k == 0:
            return s
        counts = Counter(s)
        heap = [(-cnt, ch) for ch, cnt in counts.items()]
        heapq.heapify(heap)
        queue = deque()
        res = []
        while heap:
            cnt, ch = heapq.heappop(heap)
            res.append(ch)
            queue.append((cnt + 1, ch))
            if len(queue) >= k:
                front = queue.popleft()
                if front[0] < 0:
                    heapq.heappush(heap, front)
        return ''.join(res) if len(res) == len(s) else ''
