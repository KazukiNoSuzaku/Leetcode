# Assume you are an awesome parent and want to give your children some cookies.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with.
# Each cookie j has a size s[j]. If s[j] >= g[i], we can assign cookie j to child i, and the child i will be content.
# Return the maximum number of your content children.

# Author: Kaustav Ghosh

class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        child = cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child
