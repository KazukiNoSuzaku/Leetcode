# Author: Kaustav Ghosh
# Problem: Minimum Recolors to Get K Consecutive Black Blocks
# Approach: Turning a window of k blocks all black costs one recolor per white block inside it, so slide a k-wide window over the string counting whites and keep the smallest count seen

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        whites = blocks[:k].count('W')
        best = whites
        for i in range(k, len(blocks)):
            whites += (blocks[i] == 'W') - (blocks[i - k] == 'W')
            best = min(best, whites)
        return best
