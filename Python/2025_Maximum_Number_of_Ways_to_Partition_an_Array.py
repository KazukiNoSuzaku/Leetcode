# Author: Kaustav Ghosh
# Problem: Maximum Number of Ways to Partition an Array
# Approach: A split point is valid when twice the prefix sum ending there equals the whole array's total, so the no-change answer is just how many prefix doublings already hit the total. Changing one element by some amount shifts the total by that amount and shifts every prefix that includes the element but leaves the earlier prefixes alone, which splits the condition in two: split points before the changed element need twice their prefix to equal the total plus the shift, and split points after it need twice their prefix to equal the total minus the shift. Keeping two tallies of the prefix doublings, one for the split points already passed and one for those still ahead, lets each candidate element be scored with two lookups as a single sweep moves one split point from the second tally to the first.

class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        total = len(nums)
        whole = sum(nums)

        doubled = []
        running = 0
        for index in range(total - 1):
            running += nums[index]
            doubled.append(2 * running)

        ahead = Counter(doubled)
        behind = Counter()
        best = ahead[whole]

        for index in range(total):
            shift = k - nums[index]
            count = behind[whole + shift] + ahead[whole - shift]
            if count > best:
                best = count
            if index < total - 1:
                value = doubled[index]
                ahead[value] -= 1
                behind[value] += 1
        return best
