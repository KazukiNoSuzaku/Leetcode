# Count how many stones are also jewels.

# Author: Kaustav Ghosh

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        j = set(jewels)
        return sum(s in j for s in stones)
