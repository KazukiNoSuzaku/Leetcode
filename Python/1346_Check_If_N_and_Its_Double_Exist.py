# Check if there exist two indices i != j such that arr[i] == 2 * arr[j].

# Author: Kaustav Ghosh

class Solution(object):
    def checkIfExist(self, arr):
        seen = set()
        for x in arr:
            if 2 * x in seen or (x % 2 == 0 and x // 2 in seen):
                return True
            seen.add(x)
        return False
