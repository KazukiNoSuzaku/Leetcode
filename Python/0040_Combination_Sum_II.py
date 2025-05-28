# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

# Author: Kaustav Ghosh

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort to handle duplicates and enable pruning
        result = []

        def backtrack(start, path, target_remaining):
            if target_remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursive depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If the current number exceeds the remaining target, break early
                if candidates[i] > target_remaining:
                    break
                # Include the current number and move to the next
                backtrack(i + 1, path + [candidates[i]], target_remaining - candidates[i])

        backtrack(0, [], target)
        return result
