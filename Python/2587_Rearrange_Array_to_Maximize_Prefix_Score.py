class Solution:
    def maxScore(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        prefix = 0
        score = 0
        for x in nums:
            prefix += x
            if prefix > 0:
                score += 1
            else:
                break
        return score
