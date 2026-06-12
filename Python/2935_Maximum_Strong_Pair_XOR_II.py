from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        BITS = 20
        children = [[-1, -1]]
        counts = [0]

        def insert(x: int) -> None:
            node = 0
            for i in range(BITS, -1, -1):
                b = (x >> i) & 1
                if children[node][b] == -1:
                    children[node][b] = len(children)
                    children.append([-1, -1])
                    counts.append(0)
                node = children[node][b]
                counts[node] += 1

        def remove(x: int) -> None:
            node = 0
            for i in range(BITS, -1, -1):
                node = children[node][(x >> i) & 1]
                counts[node] -= 1

        def query(x: int) -> int:
            node, res = 0, 0
            for i in range(BITS, -1, -1):
                b = (x >> i) & 1
                opp = children[node][1 - b]
                if opp != -1 and counts[opp] > 0:
                    res |= 1 << i
                    node = opp
                else:
                    node = children[node][b]
            return res

        nums.sort()
        ans = left = 0
        for y in nums:
            insert(y)
            # strong pair with x <= y requires y - x <= x, i.e. 2x >= y
            while 2 * nums[left] < y:
                remove(nums[left])
                left += 1
            ans = max(ans, query(y))
        return ans
