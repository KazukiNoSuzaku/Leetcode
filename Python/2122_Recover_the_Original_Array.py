# Author: Kaustav Ghosh
# Problem: Recover the Original Array
# Approach: Sort nums. The smallest element is a "lower" (arr[i]-k), so 2k is its gap to some other element. Try each candidate gap; for a valid k, greedily pair each smallest unused value x with x+2k, recording arr[i]=x+k. The first k that pairs everything gives a valid original

from collections import Counter

class Solution(object):
    def recoverArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        smallest = nums[0]

        for cand in range(1, n):
            diff = nums[cand] - smallest
            if diff == 0 or diff % 2 == 1:
                continue
            two_k = diff
            cnt = Counter(nums)
            result = []
            ok = True
            for x in nums:
                if cnt[x] == 0:
                    continue
                if cnt[x + two_k] == 0:
                    ok = False
                    break
                cnt[x] -= 1
                cnt[x + two_k] -= 1
                result.append(x + two_k // 2)
            if ok and len(result) == n // 2:
                return result
        return []
