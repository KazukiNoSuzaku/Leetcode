# Count numbers in [1,n] that are valid after rotating (2,5,6,9 map to different digit).

# Author: Kaustav Ghosh

class Solution(object):
    def rotatedDigits(self, n):
        valid = {'0','1','8'}
        different = {'2','5','6','9'}
        count = 0
        for x in range(1, n + 1):
            s = str(x)
            if all(c in valid or c in different for c in s) and any(c in different for c in s):
                count += 1
        return count
