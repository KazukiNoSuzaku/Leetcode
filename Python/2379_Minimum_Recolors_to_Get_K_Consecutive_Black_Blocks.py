class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks[:k].count('W')
        ans = whites
        for i in range(k, len(blocks)):
            whites += (blocks[i] == 'W') - (blocks[i - k] == 'W')
            ans = min(ans, whites)
        return ans
