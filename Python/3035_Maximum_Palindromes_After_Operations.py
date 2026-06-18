from typing import List
from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        # Any char can be swapped freely across words; collect all chars and count pairs
        total_pairs = sum(v // 2 for v in Counter(''.join(words)).values())
        ans = 0
        # Greedy: fill shortest words first (need fewer pairs)
        for word in sorted(words, key=len):
            needed = len(word) // 2
            if total_pairs >= needed:
                total_pairs -= needed
                ans += 1
            else:
                break
        return ans
