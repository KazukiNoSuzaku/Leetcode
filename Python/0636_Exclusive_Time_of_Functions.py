# Given logs of function calls, return the exclusive execution time of each function.

# Author: Kaustav Ghosh

class Solution(object):
    def exclusiveTime(self, n, logs):
        res = [0] * n
        stack = []
        prev = 0
        for log in logs:
            fid, typ, time = log.split(':')
            fid, time = int(fid), int(time)
            if typ == 'start':
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(fid)
                prev = time
            else:
                res[stack.pop()] += time - prev + 1
                prev = time + 1
        return res
