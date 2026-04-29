class Solution:
    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        first = []   # decreasing stack: waiting for 1st NGE
        second = []  # decreasing stack: waiting for 2nd NGE

        for i, x in enumerate(nums):
            # elements in second that find their 2nd NGE
            while second and nums[second[-1]] < x:
                ans[second.pop()] = x
            # elements in first that find their 1st NGE → promote to second
            promoted = []
            while first and nums[first[-1]] < x:
                promoted.append(first.pop())
            first.append(i)
            # promoted is in increasing nums order (popped from decreasing stack top);
            # reverse so second stays decreasing
            second.extend(reversed(promoted))

        return ans
