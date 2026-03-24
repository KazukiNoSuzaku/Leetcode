# Author: Kaustav Ghosh
# Problem 2014: Longest Subsequence Repeated k Times

from collections import Counter
from itertools import product

class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = Counter(s)
        # Only chars appearing >= k times can be in the answer
        candidates = sorted([ch for ch in count if count[ch] >= k], reverse=True)

        def is_subsequence_k_times(subseq, s, k):
            """Check if subseq repeated k times is a subsequence of s."""
            idx = 0
            reps = 0
            for ch in s:
                if ch == subseq[idx]:
                    idx += 1
                    if idx == len(subseq):
                        reps += 1
                        if reps == k:
                            return True
                        idx = 0
            return False

        # BFS/DFS trying longer sequences, return lexicographically largest
        from collections import deque
        best = ""
        queue = deque([""])
        while queue:
            curr = queue.popleft()
            for ch in candidates:
                new_seq = curr + ch
                if is_subsequence_k_times(new_seq, s, k):
                    if len(new_seq) > len(best) or (len(new_seq) == len(best) and new_seq > best):
                        best = new_seq
                    queue.append(new_seq)
        return best
