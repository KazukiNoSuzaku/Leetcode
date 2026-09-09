# Author: Kaustav Ghosh
# Problem: Jump Game VIII
# Approach: The two jump rules reduce to at most two forward edges per index: the ascending jump lands on the next index with a value >= nums[i] (everything between strictly smaller), and the descending jump lands on the next index with a value < nums[i] (everything between >= nums[i]). Compute both with monotonic stacks, then DP left to right for the minimum cost to reach the last index

class Solution(object):
    def minCost(self, nums, costs):
        """
        :type nums: List[int]
        :type costs: List[int]
        :rtype: int
        """
        n = len(nums)
        # next index j>i with nums[j] >= nums[i]
        nge = [-1] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            if st:
                nge[i] = st[-1]
            st.append(i)
        # next index j>i with nums[j] < nums[i]
        nl = [-1] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:
                nl[i] = st[-1]
            st.append(i)

        INF = float('inf')
        dp = [INF] * n
        dp[0] = 0
        for i in range(n):
            if dp[i] == INF:
                continue
            for j in (nge[i], nl[i]):
                if j != -1 and dp[i] + costs[j] < dp[j]:
                    dp[j] = dp[i] + costs[j]
        return dp[n - 1]
