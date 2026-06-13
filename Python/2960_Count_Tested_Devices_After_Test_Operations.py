from typing import List

class Solution:
    def countTestedDevices(self, batteries: List[int]) -> int:
        tested = 0
        for b in batteries:
            if b > tested:
                tested += 1
        return tested
