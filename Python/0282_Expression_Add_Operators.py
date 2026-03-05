# Given a string num that contains only digits and an integer target, return all possibilities
# to insert the binary operators '+', '-', or '*' between the digits of num so that the
# resultant expression evaluates to the target value.

# Example 1:
# Input: num = "123", target = 6
# Output: ["1+2+3","1*2*3"]

# Example 2:
# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]

# Constraints:
# 1 <= num.length <= 10
# num consists of only digits.
# -2^31 <= target <= 2^31 - 1

# Author: Kaustav Ghosh

class Solution(object):
    def addOperators(self, num, target):
        res = []
        def dfs(idx, path, val, prev):
            if idx == len(num):
                if val == target:
                    res.append(path)
                return
            for i in range(idx, len(num)):
                s = num[idx:i+1]
                n = int(s)
                if len(s) > 1 and s[0] == '0':
                    break
                if idx == 0:
                    dfs(i+1, s, n, n)
                else:
                    dfs(i+1, path+'+'+s, val+n, n)
                    dfs(i+1, path+'-'+s, val-n, -n)
                    dfs(i+1, path+'*'+s, val-prev+prev*n, prev*n)
        dfs(0, '', 0, 0)
        return res
