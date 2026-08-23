# Author: Kaustav Ghosh
# Problem: Sum of Subarray Ranges
# Approach: The answer is the sum of subarray maxima minus the sum of subarray minima. Each value's contribution is (span to the left)*(span to the right), computed with monotonic stacks and strict/non-strict boundaries to avoid double counting equal values

class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        def contribution(sign):
            # sign=+1 -> sum of maxima; sign=-1 -> sum of minima
            total = 0
            left = [0] * n
            right = [0] * n
            st = []
            for i in range(n):
                while st and sign * nums[st[-1]] < sign * nums[i]:
                    st.pop()
                left[i] = i - (st[-1] if st else -1)
                st.append(i)
            st = []
            for i in range(n - 1, -1, -1):
                while st and sign * nums[st[-1]] <= sign * nums[i]:
                    st.pop()
                right[i] = (st[-1] if st else n) - i
                st.append(i)
            for i in range(n):
                total += nums[i] * left[i] * right[i]
            return total

        return contribution(1) - contribution(-1)
