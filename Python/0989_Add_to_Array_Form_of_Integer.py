# The array-form of integer is its digits in an array.
# Return the array-form of num + k.

# Author: Kaustav Ghosh

class Solution(object):
    def addToArrayForm(self, num, k):
        num[-1] += k
        i = len(num) - 1
        while i > 0 and num[i] >= 10:
            num[i-1] += num[i] // 10
            num[i] %= 10
            i -= 1
        return ([int(d) for d in str(num[0])] + num[1:]) if num[0] >= 10 else num
