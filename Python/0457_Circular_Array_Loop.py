# You are playing a game involving a circular array of non-zero integers nums.
# Return true if there exists a cycle in nums. A cycle must have the same direction,
# length >= 2, and only elements within the cycle.

# Author: Kaustav Ghosh

class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_idx(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue
            slow, fast = i, i
            while nums[slow] * nums[next_idx(slow)] > 0 and nums[fast] * nums[next_idx(fast)] > 0 and nums[fast] * nums[next_idx(next_idx(fast))] > 0:
                slow = next_idx(slow)
                fast = next_idx(next_idx(fast))
                if slow == fast:
                    if slow == next_idx(slow):
                        break
                    return True
            # Mark visited with 0
            j = i
            while nums[j] * nums[next_idx(j)] > 0:
                nxt = next_idx(j)
                nums[j] = 0
                j = nxt
        return False
