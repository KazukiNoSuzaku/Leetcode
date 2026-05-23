class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        seen_a, seen_b = set(), set()
        ans = []
        common = 0
        for a, b in zip(A, B):
            seen_a.add(a)
            if a in seen_b:
                common += 1
            seen_b.add(b)
            if b in seen_a and b != a:
                common += 1
            ans.append(common)
        return ans
