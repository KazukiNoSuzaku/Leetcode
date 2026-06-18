from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        carried = 0
        for i, cap in enumerate(capacity):
            carried += cap
            if carried >= total:
                return i + 1
        return len(capacity)
