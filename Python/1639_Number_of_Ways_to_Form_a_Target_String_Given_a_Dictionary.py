# Author: Kaustav Ghosh
# Problem: Number of Ways to Form a Target String Given a Dictionary
# Approach: Because every chosen character must come from a strictly later column than the one before it, the identity of the word a character came from never matters again, only how many words offer that character in that column; tallying those counts per column once collapses the whole dictionary into a small table. The count then sweeps the columns left to right carrying, for each number of target characters matched so far, how many ways there are to have matched them, and at each column either skips it or consumes it to match the next target character, multiplying by how many words supply it. Updating the running array from the back lets one array serve both the previous and the current column.

class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        width = len(words[0])
        n = len(target)
        if n > width:
            return 0

        available = [[0] * 26 for _ in range(width)]
        for word in words:
            for column, ch in enumerate(word):
                available[column][ord(ch) - 97] += 1

        wanted = [ord(ch) - 97 for ch in target]
        ways = [0] * (n + 1)
        ways[0] = 1
        for column in range(width):
            counts = available[column]
            top = n - 1 if n - 1 < column else column
            for matched in range(top, -1, -1):
                supply = counts[wanted[matched]]
                if supply and ways[matched]:
                    ways[matched + 1] = (ways[matched + 1] + ways[matched] * supply) % MOD
        return ways[n]
