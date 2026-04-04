# Author: Kaustav Ghosh

class Solution(object):
    def minimalKSum(self, nums, k):
        # type: (List[int], int) -> int
        nums = sorted(set(nums))
        result = 0
        current = 1

        for num in nums:
            if k <= 0:
                break
            if num > current:
                # We can take min(k, num - current) integers from [current, num-1]
                count = min(k, num - current)
                # Sum of arithmetic sequence: count * current + count*(count-1)//2
                result += count * current + count * (count - 1) // 2
                k -= count
            current = num + 1

        # If we still need more integers after all nums
        if k > 0:
            result += k * current + k * (k - 1) // 2

        return result
