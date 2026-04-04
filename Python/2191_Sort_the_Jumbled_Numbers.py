# Author: Kaustav Ghosh

class Solution(object):
    def sortJumbled(self, mapping, nums):
        # type: (List[int], List[int]) -> List[int]
        def convert(n):
            if n == 0:
                return mapping[0]
            result = 0
            factor = 1
            while n > 0:
                result += mapping[n % 10] * factor
                factor *= 10
                n //= 10
            return result

        return sorted(nums, key=lambda x: convert(x))
